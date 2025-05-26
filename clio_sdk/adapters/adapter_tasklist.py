# Adapter for tasklist
from clio_sdk.models.tasklist import TasklistIn, TasklistOut, TasklistUpdate, TasklistDb
from clio_client.models.task_list import TaskList

def convert_sdk_to_tasklistout(src: TaskList) -> TasklistOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasklistOut(**src.model_dump())

def convert_tasklistin_to_sdk(src: TasklistIn) -> TaskList:
    """Converts a clio_sdk model to clio_client model."""
    return TaskList(**src.model_dump())
