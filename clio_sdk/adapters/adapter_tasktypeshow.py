# Adapter for tasktypeshow
from clio_sdk.models.tasktypeshow import TasktypeshowIn, TasktypeshowOut, TasktypeshowUpdate, TasktypeshowDb
from clio_client.models.task_type_show import TaskTypeShow

def convert_sdk_to_tasktypeshowout(src: TaskTypeShow) -> TasktypeshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktypeshowOut(**src.model_dump())

def convert_tasktypeshowin_to_sdk(src: TasktypeshowIn) -> TaskTypeShow:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTypeShow(**src.model_dump())
