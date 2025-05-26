.PHONY: help init audit validate refactor bundle merge deref generate derive lint clean

# File paths
ROOT_YAML=openapi/root.yaml
FINAL_BUNDLE=openapi/final_bundle.yaml
FINAL_MERGED=openapi/final_merged.yaml
EXPANDED=openapi/expanded.yaml
DEREF=openapi/dereferenced.yaml
COMPONENTS_DIR=openapi/components
PATHS_DIR=openapi/paths

help:
	@echo "📘 OpenAPI Modular Pipeline"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Init and Setup:"
	@echo "  init            Create necessary folders for modular OpenAPI structure"
	@echo ""
	@echo "Audit and Validation:"
	@echo "  audit           Validate individual files (paths, components)"
	@echo "  validate        Validate bundled requestBodies.yaml and components.yaml"
	@echo ""
	@echo "Refactor and Normalize:"
	@echo "  refactor        Normalize, fix types, deduplicate, patch top-level spec"
	@echo ""
	@echo "Bundle and Wrap:"
	@echo "  bundle          Bundle parameters, responses, schemas, and requestBodies"
	@echo ""
	@echo "Merge and Expand:"
	@echo "  merge           Merge paths + components into root spec"
	@echo "  deref           Deep-dereference full spec"
	@echo ""
	@echo "Generate and Lint:"
	@echo "  generate        Generate Pydantic models and adapters"
	@echo "  derive          Derive API call suggestions from modular components"
	@echo "  lint            Run Spectral linting"
	@echo "  clean           Remove generated artifacts"

init:
	@echo "📁 Initializing OpenAPI directory structure..."
	@mkdir -p openapi/components/{parameters,responses,schemas,requestBodies} openapi/paths

audit:
	@echo "🔍 Auditing modular structure and component integrity..."
	python3 scripts/validate_paths.py
	python3 scripts/validate_parameters.py
	python3 scripts/validate_responses.py
	python3 scripts/validate_request_bodies.py
	python3 scripts/validate_schemas.py
	python3 scripts/audit_missing_types.py
	python3 scripts/audit_for_content.py

validate:
	@echo "📦 Validating bundled components and request bodies..."
	python3 scripts/validate_components_yaml.py
	python3 scripts/validate_request_bodies_yaml.py

refactor:
	@echo "🔧 Refactoring modular OpenAPI files..."
	python3 scripts/rename_operation_ids.py
	python3 scripts/rename_request_bodies_by_description.py
	python3 scripts/fix_missing_schema_types.py
	python3 scripts/clean_parameters.py
	python3 scripts/wrap_paths_only.py
	python3 scripts/wrap_unnamed_schemas.py
	python3 scripts/add_oauth2_security.py
	python3 scripts/fix_top_level.py

bundle:
	@echo "📦 Bundling all component types into master YAML files..."
	python3 scripts/bundle_parameters.py
	python3 scripts/bundle_responses.py
	python3 scripts/bundle_request_bodies.py
	python3 scripts/bundle_schemas.py
	python3 scripts/bundle_components_into_master.py

merge:
	@echo "🧩 Merging components and paths into final OpenAPI spec..."
	python3 scripts/merge_all_into_root.py
	python3 scripts/merge_paths_into_spec.py

deref:
	@echo "🔎 Dereferencing $refs for full schema resolution..."
	python3 scripts/deref_paths.py --input $(FINAL_MERGED) --output $(DEREF)

generate:
	@echo "🧬 Generating models and adapters from full spec..."
	python3 scripts/generate_models_from_openapi.py

derive:
	@echo "📡 Deriving inferred API operations from modular definitions..."
	python3 scripts/derive_api_calls.py

lint:
	@echo "🧹 Running Spectral lint on all OpenAPI files..."
	npx spectral lint openapi/**/*.yaml --ruleset .spectral.yaml

clean:
	@echo "🧽 Cleaning generated output..."
	rm -f $(FINAL_BUNDLE) $(FINAL_MERGED) $(EXPANDED) $(DEREF)
	rm -rf schemas/from_expanded adapters/from_expanded
