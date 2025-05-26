# Adapter for tasktypebase
from clio_sdk.models.tasktypebase import TasktypeBaseIn, TasktypebaseOut, TasktypebaseUpdate, TasktypebaseDb
from clio_client.models.task_type import TaskType

def convert_sdk_to_tasktypebaseout(src: TaskType) -> TasktypebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktypebaseOut(**src.model_dump())

def convert_tasktypebasein_to_sdk(src: TasktypeBaseIn) -> TaskType:
    """Converts a clio_sdk model to clio_client model."""
    return TaskType(**src.model_dump())
