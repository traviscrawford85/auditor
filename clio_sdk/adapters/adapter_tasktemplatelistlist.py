# Adapter for tasktemplatelistlist
from clio_sdk.models.tasktemplatelistlist import TasktemplatelistlistIn, TasktemplatelistlistOut, TasktemplatelistlistUpdate, TasktemplatelistlistDb
from clio_client.models import task_template_list_list

def convert_sdk_to_tasktemplatelistlistout(src: task_template_list_list) -> TasktemplatelistlistOut:
    return TasktemplatelistlistOut(**src.dict())

def convert_tasktemplatelistlistin_to_sdk(src: TasktemplatelistlistIn) -> task_template_list_list:
    return task_template_list_list(**src.dict())
