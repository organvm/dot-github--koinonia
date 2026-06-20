.PHONY: test unit validate-yaml secret-scan

test: unit validate-yaml secret-scan

unit:
	python3 -m unittest discover -s tests -v

validate-yaml:
	python3 -c 'from pathlib import Path; import yaml; paths=[p for p in sorted(Path(".").glob("**/*.yml")) + sorted(Path(".").glob("**/*.yaml")) if ".git" not in p.parts]; [yaml.safe_load(p.read_text()) for p in paths]; print(f"validated {len(paths)} YAML files")'

secret-scan:
	@FOUND=0; \
	for pattern in 'sk-[a-zA-Z0-9]{20,}' 'ghp_[a-zA-Z0-9]{36}' 'AKIA[A-Z0-9]{16}'; do \
		if git grep -lP "$$pattern" -- ':!.github' 2>/dev/null; then \
			echo "::error::Potential secret pattern found: $$pattern"; \
			FOUND=1; \
		fi; \
	done; \
	if [ "$$FOUND" -eq 1 ]; then exit 1; fi; \
	echo "No secret patterns detected"
