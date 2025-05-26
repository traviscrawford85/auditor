# Adapter for tasktemplatelist
from clio_sdk.models.tasktemplatelist import TasktemplatelistIn, TasktemplatelistOut, TasktemplatelistUpdate, TasktemplatelistDb
from clio_client.models import task_template_list

def convert_sdk_to_tasktemplatelistout(src: task_template_list) -> TasktemplatelistOut:
    return TasktemplatelistOut(**src.dict())

def convert_tasktemplatelistin_to_sdk(src: TasktemplatelistIn) -> task_template_list:
    return task_template_list(**src.dict())
