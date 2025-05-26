# Adapter for taskbase
from clio_sdk.models.taskbase import TaskbaseIn, TaskbaseOut, TaskbaseUpdate, TaskbaseDb
from clio_client.models import task

def convert_sdk_to_taskbaseout(src: task) -> TaskbaseOut:
    return TaskbaseOut(**src.dict())

def convert_taskbasein_to_sdk(src: TaskbaseIn) -> task:
    return task(**src.dict())
