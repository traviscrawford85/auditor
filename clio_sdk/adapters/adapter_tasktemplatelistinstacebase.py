# Adapter for tasktemplatelistinstacebase
from clio_sdk.models.tasktemplatelistinstacebase import TasktemplatelistinstaceBaseIn, TasktemplatelistinstacebaseOut, TasktemplatelistinstacebaseUpdate, TasktemplatelistinstacebaseDb
from clio_client.models.task_template_list_instace_base import TaskTemplateListInstaceBase

def convert_sdk_to_tasktemplatelistinstacebaseout(src: TaskTemplateListInstaceBase) -> TasktemplatelistinstacebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktemplatelistinstacebaseOut(**src.model_dump())

def convert_tasktemplatelistinstacebasein_to_sdk(src: TasktemplatelistinstaceBaseIn) -> TaskTemplateListInstaceBase:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTemplateListInstaceBase(**src.model_dump())
