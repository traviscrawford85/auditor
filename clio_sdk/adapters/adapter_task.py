"""
This file contains bidirectional adapters that translate between Clio SDK models and clio_client models.

Adapters are responsible for:
- Converting verbose and fragmented OpenAPI-generated models into streamlined SDK models.
- Abstracting away internal structural differences like nested fields and enum values.
- Handling inconsistencies, optional fields, and naming conventions between layers.

Copilot Prompt:
- Implement `from_taskshow()` to convert a clio_client TaskShow model into an SDK-level Task.
- Create similar functions like `to_taskcreate_json_body()` if needed for write operations.
- Use `.value` for enum conversions and guard against missing nested structures (e.g., task.matter?.id).
- The goal is to decouple SDK usage from clio_client schema details.
"""


from clio_client.models.task_show import TaskShow
from clio_sdk.models.task import Task


def from_taskshow(task: TaskShow) -> Task:
    return Task(
        id=task.id,
        description=task.description,
        status=task.status.value if task.status else None,
        priority=task.priority.value if task.priority else None,
        due_date=task.due_date,
        matter_id=task.matter.id if task.matter else None,
        assignee_id=task.assignee.id if task.assignee else None,
        created_by=task.assigner.id if task.assigner else None,
    )

