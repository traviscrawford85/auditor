OPENAPI_DIR=./openapi

.PHONY: all audit lint refs normalize rename prepend

all: audit

audit: prepend lint refs

prepend:
	@echo "🔧 Prepending Copilot prompt to OpenAPI files..."
	python3 scripts/prepend_copilot_prompt.py

lint:
	@echo "🧹 Linting for unused components..."
	python3 scripts/lint_openapi.py

refs:
	@echo "🔍 Validating $ref integrity..."
	python3 scripts/validate_refs_extended.py

normalize:
	@echo "🧼 Normalizing paths and operationIds..."
	python3 scripts/normalize_openapi.py

rename:
	@echo "✏️ Renaming request bodies based on description..."
	python3 scripts/rename_request_bodies_by_description.py
