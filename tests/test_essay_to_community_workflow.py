import json
import os
import shutil
import subprocess
import textwrap
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "essay-to-community.yml"


class WorkflowLoader(yaml.SafeLoader):
    pass


WorkflowLoader.yaml_implicit_resolvers = {
    key: [
        resolver
        for resolver in resolvers
        if resolver[0] != "tag:yaml.org,2002:bool"
    ]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load_workflow():
    return yaml.load(WORKFLOW_PATH.read_text(), Loader=WorkflowLoader)


def find_step(workflow, job_name, step_name):
    for step in workflow["jobs"][job_name]["steps"]:
        if step.get("name") == step_name:
            return step
    raise AssertionError(f"missing step {step_name!r} in job {job_name!r}")


def parse_github_output(path):
    output = {}
    for line in path.read_text().splitlines():
        if not line:
            continue
        key, value = line.split("=", 1)
        output[key] = value
    return output


def write_executable(path, content):
    content = content.strip("\n")
    if content.startswith("#!") and "\n" in content:
        shebang, body = content.split("\n", 1)
        content = f"{shebang}\n{textwrap.dedent(body)}"
    else:
        content = textwrap.dedent(content)
    path.write_text(f"{content.rstrip()}\n")
    path.chmod(0o755)


class EssayToCommunityWorkflowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = load_workflow()

    def run_bash(self, script, cwd, env=None):
        full_env = os.environ.copy()
        full_env.update(env or {})
        result = subprocess.run(
            ["bash", "-e", "-u", "-o", "pipefail", "-c", script],
            cwd=cwd,
            env=full_env,
            text=True,
            capture_output=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            f"script failed with {result.returncode}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
        )
        return result

    def test_workflow_routes_only_essay_events_and_daily_poll(self):
        triggers = self.workflow["on"]
        self.assertEqual(triggers["repository_dispatch"]["types"], ["essay-published"])
        self.assertEqual(triggers["schedule"], [{"cron": "0 11 * * *"}])
        self.assertIn("workflow_dispatch", triggers)

        dispatch_job = self.workflow["jobs"]["handle-dispatch"]
        self.assertEqual(dispatch_job["if"], "github.event_name == 'repository_dispatch'")
        self.assertEqual(dispatch_job["permissions"], {"issues": "write"})

        poll_job = self.workflow["jobs"]["handle-poll"]
        self.assertEqual(
            poll_job["if"],
            "github.event_name == 'schedule' || github.event_name == 'workflow_dispatch'",
        )
        self.assertEqual(poll_job["permissions"], {"issues": "write"})

    def test_dispatch_extract_step_maps_payload_and_defaults(self):
        self.assertIsNotNone(shutil.which("jq"), "jq is required by the workflow")
        script = find_step(
            self.workflow, "handle-dispatch", "Extract essay details"
        )["run"]

        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            output_path = tmp_path / "github-output"
            payload = {
                "essay_title": "Living Systems Ignite",
                "essay_url": "https://example.test/essay",
                "essay_date": "2026-06-20",
                "source_repo": "organvm-v-logos/public-process",
            }
            self.run_bash(
                script,
                tmp_path,
                {
                    "EVENT_PAYLOAD": json.dumps(payload),
                    "GITHUB_OUTPUT": str(output_path),
                },
            )

            self.assertEqual(
                parse_github_output(output_path),
                {
                    "title": "Living Systems Ignite",
                    "url": "https://example.test/essay",
                    "date": "2026-06-20",
                    "source": "organvm-v-logos/public-process",
                },
            )

            output_path.write_text("")
            self.run_bash(
                script,
                tmp_path,
                {"EVENT_PAYLOAD": "{}", "GITHUB_OUTPUT": str(output_path)},
            )
            self.assertEqual(
                parse_github_output(output_path),
                {
                    "title": "Untitled",
                    "url": "",
                    "date": "",
                    "source": "organvm-v-logos/public-process",
                },
            )

    def test_dispatch_duplicate_check_uses_existing_issue_titles(self):
        script = find_step(
            self.workflow, "handle-dispatch", "Check for existing tracking issue"
        )["run"]

        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bin_dir = tmp_path / "bin"
            bin_dir.mkdir()
            write_executable(
                bin_dir / "gh",
                """#!/usr/bin/env python3
                import os
                print(os.environ["GH_ISSUE_LIST_RESPONSE"])
                """,
            )
            env = {
                "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
                "ESSAY_TITLE": "Living Systems Ignite",
            }

            output_path = tmp_path / "existing-output"
            self.run_bash(
                script,
                tmp_path,
                {
                    **env,
                    "GITHUB_OUTPUT": str(output_path),
                    "GH_ISSUE_LIST_RESPONSE": json.dumps(
                        [{"title": "Essay Review: Living Systems Ignite"}]
                    ),
                },
            )
            self.assertEqual(parse_github_output(output_path), {"exists": "true"})

            output_path.write_text("")
            self.run_bash(
                script,
                tmp_path,
                {
                    **env,
                    "GITHUB_OUTPUT": str(output_path),
                    "GH_ISSUE_LIST_RESPONSE": "[]",
                },
            )
            self.assertEqual(parse_github_output(output_path), {"exists": "false"})

    def test_dispatch_create_step_builds_curator_issue(self):
        script = find_step(
            self.workflow, "handle-dispatch", "Create tracking issue"
        )["run"]

        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bin_dir = tmp_path / "bin"
            bin_dir.mkdir()
            capture_path = tmp_path / "created-issue.json"
            write_executable(
                bin_dir / "gh",
                """#!/usr/bin/env python3
                import json
                import os
                import sys
                from pathlib import Path

                body_file = Path(sys.argv[sys.argv.index("--body-file") + 1])
                Path(os.environ["GH_CAPTURE"]).write_text(json.dumps({
                    "argv": sys.argv[1:],
                    "body": body_file.read_text(),
                }))
                """,
            )

            self.run_bash(
                script,
                tmp_path,
                {
                    "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
                    "GH_CAPTURE": str(capture_path),
                    "ESSAY_TITLE": "Living Systems Ignite",
                    "ESSAY_URL": "https://example.test/essay",
                    "ESSAY_DATE": "2026-06-20",
                    "ESSAY_SOURCE": "organvm-v-logos/public-process",
                },
            )

            created = json.loads(capture_path.read_text())
            self.assertIn("--repo", created["argv"])
            self.assertIn("organvm-vi-koinonia/reading-group-curriculum", created["argv"])
            self.assertIn("--title", created["argv"])
            self.assertIn("Essay Review: Living Systems Ignite", created["argv"])
            self.assertEqual(created["argv"].count("--label"), 2)
            self.assertIn("essay-review", created["argv"])
            self.assertIn("from-logos", created["argv"])
            self.assertIn("## New Essay for Community Review", created["body"])
            self.assertIn("**URL:** https://example.test/essay", created["body"])
            self.assertIn("Adaptive syllabus recommendations", created["body"])

    def test_poll_step_creates_recent_missing_issues_and_skips_existing(self):
        script = find_step(
            self.workflow, "handle-poll", "Poll for recent essays"
        )["run"]

        today = datetime.now(timezone.utc).date()
        yesterday = today - timedelta(days=1)
        old = today - timedelta(days=3)
        posts = [
            {"name": f"{today:%Y-%m-%d}-emergent-community.md"},
            {"name": f"{yesterday:%Y-%m-%d}-already-reviewed.md"},
            {"name": f"{old:%Y-%m-%d}-stale-essay.md"},
            {"name": "README.txt"},
            {"name": "not-a-date.md"},
        ]

        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bin_dir = tmp_path / "bin"
            capture_dir = tmp_path / "captures"
            bin_dir.mkdir()
            capture_dir.mkdir()
            write_executable(
                bin_dir / "gh",
                """#!/usr/bin/env python3
                import json
                import os
                import sys
                from pathlib import Path

                capture_dir = Path(os.environ["GH_CAPTURE_DIR"])

                if sys.argv[1] == "api":
                    print(os.environ["POSTS_JSON"])
                    sys.exit(0)

                if sys.argv[1:3] == ["issue", "list"]:
                    search = sys.argv[sys.argv.index("--search") + 1]
                    existing_titles = json.loads(os.environ["EXISTING_TITLES"])
                    if any(title in search for title in existing_titles):
                        print(json.dumps([{"title": f"Essay Review: {existing_titles[0]}"}]))
                    else:
                        print("[]")
                    sys.exit(0)

                if sys.argv[1:3] == ["issue", "create"]:
                    body_file = Path(sys.argv[sys.argv.index("--body-file") + 1])
                    index = len(list(capture_dir.glob("create-*.json"))) + 1
                    (capture_dir / f"create-{index}.json").write_text(json.dumps({
                        "argv": sys.argv[1:],
                        "body": body_file.read_text(),
                    }))
                    sys.exit(0)

                print(f"unexpected gh invocation: {sys.argv}", file=sys.stderr)
                sys.exit(2)
                """,
            )

            output_path = tmp_path / "github-output"
            result = self.run_bash(
                script,
                tmp_path,
                {
                    "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
                    "GH_CAPTURE_DIR": str(capture_dir),
                    "GITHUB_OUTPUT": str(output_path),
                    "POSTS_JSON": json.dumps(posts),
                    "EXISTING_TITLES": json.dumps(["Already Reviewed"]),
                },
            )

            self.assertEqual(parse_github_output(output_path), {"essay_count": "2"})
            self.assertIn("Processed 2 recent essays", result.stdout)

            created_files = sorted(capture_dir.glob("create-*.json"))
            self.assertEqual(len(created_files), 1)
            created = json.loads(created_files[0].read_text())
            self.assertIn("Essay Review: Emergent Community", created["argv"])
            self.assertNotIn("Already Reviewed", created["body"])
            self.assertIn("**Source:** organvm-v-logos/public-process", created["body"])
