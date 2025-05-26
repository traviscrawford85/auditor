# Adapter for tasktypelist
from clio_sdk.models.tasktypelist import TasktypelistIn, TasktypelistOut, TasktypelistUpdate, TasktypelistDb
from clio_client.models import task_type_list

def convert_sdk_to_tasktypelistout(src: task_type_list) -> TasktypelistOut:
    return TasktypelistOut(**src.dict())

def convert_tasktypelistin_to_sdk(src: TasktypelistIn) -> task_type_list:
    return task_type_list(**src.dict())
