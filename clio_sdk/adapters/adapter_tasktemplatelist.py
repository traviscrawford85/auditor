# Adapter for tasktemplatelist
from clio_sdk.models.tasktemplatelist import TasktemplatelistIn, TasktemplatelistOut, TasktemplatelistUpdate, TasktemplatelistDb
from clio_client.models.task_template_list import TaskTemplateList

def convert_sdk_to_tasktemplatelistout(src: TaskTemplateList) -> TasktemplatelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktemplatelistOut(**src.model_dump())

def convert_tasktemplatelistin_to_sdk(src: TasktemplatelistIn) -> TaskTemplateList:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTemplateList(**src.model_dump())
