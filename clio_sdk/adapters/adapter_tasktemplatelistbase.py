# Adapter for tasktemplatelistbase
from clio_sdk.models.tasktemplatelistbase import TasktemplatelistBaseIn, TasktemplatelistbaseOut, TasktemplatelistbaseUpdate, TasktemplatelistbaseDb
from clio_client.models.task_template_list import TaskTemplateList

def convert_sdk_to_tasktemplatelistbaseout(src: TaskTemplateList) -> TasktemplatelistbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktemplatelistbaseOut(**src.model_dump())

def convert_tasktemplatelistbasein_to_sdk(src: TasktemplatelistBaseIn) -> TaskTemplateList:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTemplateList(**src.model_dump())
