# Adapter for tasktemplatelistinstacebase
from clio_sdk.models.tasktemplatelistinstacebase import TasktemplatelistinstacebaseIn, TasktemplatelistinstacebaseOut, TasktemplatelistinstacebaseUpdate, TasktemplatelistinstacebaseDb
from clio_client.models import task_template_list_instace_base

def convert_sdk_to_tasktemplatelistinstacebaseout(src: task_template_list_instace_base) -> TasktemplatelistinstacebaseOut:
    return TasktemplatelistinstacebaseOut(**src.dict())

def convert_tasktemplatelistinstacebasein_to_sdk(src: TasktemplatelistinstacebaseIn) -> task_template_list_instace_base:
    return task_template_list_instace_base(**src.dict())
