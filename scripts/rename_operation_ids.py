import argparse
import yaml
from pathlib import Path

def rename_operation_ids(spec: dict, style: str = 'underscore') -> dict:
    for path, operations in spec.get('paths', {}).items():
        for method, operation in operations.items():
            if isinstance(operation, dict) and 'operationId' not in operation:
                base = path.strip('/').replace('/', '_').replace('{', '').replace('}', '')
                if style == 'underscore':
                    op_id = f"{method}_{base}"
                else:
                    op_id = f"{method}{base.title().replace('_', '')}"
                operation['operationId'] = op_id
    return spec

def process_file(file_path: Path, style: str):
    with file_path.open() as f:
        spec = yaml.safe_load(f)

    updated_spec = rename_operation_ids(spec, style=style)

    with file_path.open('w') as f:
        yaml.safe_dump(updated_spec, f, sort_keys=False)
