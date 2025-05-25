.PHONY: help all patch expand deref generate audit-prep audit-lint audit-fix audit

# Default target
help:
	@echo "🔧 OpenAPI Automation Pipeline"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  help         Show this help message"
	@echo "  all          Run full pipeline: patch → expand → deref → generate"
	@echo "  patch        Merge full components into root spec"
	@echo "  expand       Merge $refs in components into root"
	@echo "  deref        Deep dereference $refs in paths and components"
	@echo "  generate     Generate Pydantic models and adapter stubs"
	@echo "  audit-prep   Prepend Copilot audit prompt to each YAML file"
	@echo "  audit-lint   Lint YAML files using Spectral and custom ruleset"
	@echo "  audit-fix    Attempt minor Spectral auto-fixes (if applicable)"
	@echo "  audit        Full audit: audit-prep + audit-lint"

# Paths
ROOT_YAML=openapi/root.yaml
PATCHED_YAML=openapi/root.patched.yaml
EXPANDED_YAML=openapi/expanded.yaml
EXPANDED_FULL=openapi/expanded_full.yaml
COMPONENTS_DIR=openapi/components

# Targets
all: patch expand deref generate

# Lint all YAML specs using spectral and your custom ruleset
audit-lint:
	@echo "🔍 Running Spectral lint across openapi/**/*.yaml..."
	npx spectral lint openapi/**/*.yaml --ruleset .spectral.yaml

# (Optional) Fix minor issues using spectral if applicable
audit-fix:
	@echo "🛠  Attempting automatic fixes with Spectral (limited support)..."
	npx spectral lint openapi/**/*.yaml --ruleset .spectral.yaml --format json | jq -r '.[] | select(.code == "info-contact") | .location.start.line' # Example

# Combined prep + lint
audit: audit-prep audit-lint


patch:
	@echo "🔧 Patching root.yaml with full components..."
	python3 scripts/patch_root.py --input $(ROOT_YAML) --original openapi.json --output $(PATCHED_YAML)

expand:
	@echo "🔄 Expanding component refs into root..."
	python3 scripts/expand_refs_merge.py --input $(PATCHED_YAML) --components-dir $(COMPONENTS_DIR) --output $(EXPANDED_YAML)

deref:
	@echo "🧠 Dereferencing paths and components..."
	python3 scripts/deref_paths.py --input $(EXPANDED_YAML) --output $(EXPANDED_FULL)

generate:
	@echo "🧬 Generating Pydantic models..."
	python3 generate_models_from_expanded.py
