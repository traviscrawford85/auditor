# Adapter for taskshow
from clio_sdk.models.taskshow import TaskshowIn, TaskshowOut, TaskshowUpdate, TaskshowDb
from clio_client.models.task_show import TaskShow

def convert_sdk_to_taskshowout(src: TaskShow) -> TaskshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TaskshowOut(**src.model_dump())

def convert_taskshowin_to_sdk(src: TaskshowIn) -> TaskShow:
    """Converts a clio_sdk model to clio_client model."""
    return TaskShow(**src.model_dump())
