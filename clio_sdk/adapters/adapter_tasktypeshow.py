# Adapter for tasktypeshow
from clio_sdk.models.tasktypeshow import TasktypeshowIn, TasktypeshowOut, TasktypeshowUpdate, TasktypeshowDb
from clio_client.models import task_type_show

def convert_sdk_to_tasktypeshowout(src: task_type_show) -> TasktypeshowOut:
    return TasktypeshowOut(**src.dict())

def convert_tasktypeshowin_to_sdk(src: TasktypeshowIn) -> task_type_show:
    return task_type_show(**src.dict())
