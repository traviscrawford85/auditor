# Adapter for tasktemplatelistlist
from clio_sdk.models.tasktemplatelistlist import TasktemplatelistlistIn, TasktemplatelistlistOut, TasktemplatelistlistUpdate, TasktemplatelistlistDb
from clio_client.models.task_template_list_list import TaskTemplateListList

def convert_sdk_to_tasktemplatelistlistout(src: TaskTemplateListList) -> TasktemplatelistlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktemplatelistlistOut(**src.model_dump())

def convert_tasktemplatelistlistin_to_sdk(src: TasktemplatelistlistIn) -> TaskTemplateListList:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTemplateListList(**src.model_dump())
