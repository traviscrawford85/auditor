# Adapter for tasktemplatelistbase
from clio_sdk.models.tasktemplatelistbase import TasktemplatelistbaseIn, TasktemplatelistbaseOut, TasktemplatelistbaseUpdate, TasktemplatelistbaseDb
from clio_client.models import task_template_list

def convert_sdk_to_tasktemplatelistbaseout(src: task_template_list) -> TasktemplatelistbaseOut:
    return TasktemplatelistbaseOut(**src.dict())

def convert_tasktemplatelistbasein_to_sdk(src: TasktemplatelistbaseIn) -> task_template_list:
    return task_template_list(**src.dict())
