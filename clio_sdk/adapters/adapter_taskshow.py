# Adapter for taskshow
from clio_sdk.models.taskshow import TaskshowIn, TaskshowOut, TaskshowUpdate, TaskshowDb
from clio_client.models import task_show

def convert_sdk_to_taskshowout(src: task_show) -> TaskshowOut:
    return TaskshowOut(**src.dict())

def convert_taskshowin_to_sdk(src: TaskshowIn) -> task_show:
    return task_show(**src.dict())
