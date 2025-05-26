# Adapter for tasktypebase
from clio_sdk.models.tasktypebase import TasktypebaseIn, TasktypebaseOut, TasktypebaseUpdate, TasktypebaseDb
from clio_client.models import task_type

def convert_sdk_to_tasktypebaseout(src: task_type) -> TasktypebaseOut:
    return TasktypebaseOut(**src.dict())

def convert_tasktypebasein_to_sdk(src: TasktypebaseIn) -> task_type:
    return task_type(**src.dict())
