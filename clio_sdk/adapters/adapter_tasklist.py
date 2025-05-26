# Adapter for tasklist
from clio_sdk.models.tasklist import TasklistIn, TasklistOut, TasklistUpdate, TasklistDb
from clio_client.models import task_list

def convert_sdk_to_tasklistout(src: task_list) -> TasklistOut:
    return TasklistOut(**src.dict())

def convert_tasklistin_to_sdk(src: TasklistIn) -> task_list:
    return task_list(**src.dict())
