# Adapter for taskbase
from clio_sdk.models.taskbase import TaskBaseIn, TaskbaseOut, TaskbaseUpdate, TaskbaseDb
from clio_client.models.task import Task

def convert_sdk_to_taskbaseout(src: Task) -> TaskbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TaskbaseOut(**src.model_dump())

def convert_taskbasein_to_sdk(src: TaskBaseIn) -> Task:
    """Converts a clio_sdk model to clio_client model."""
    return Task(**src.model_dump())
