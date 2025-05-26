# Adapter for tasktemplatelistshow
from clio_sdk.models.tasktemplatelistshow import TasktemplatelistshowIn, TasktemplatelistshowOut, TasktemplatelistshowUpdate, TasktemplatelistshowDb
from clio_client.models.task_template_list_show import TaskTemplateListShow

def convert_sdk_to_tasktemplatelistshowout(src: TaskTemplateListShow) -> TasktemplatelistshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktemplatelistshowOut(**src.model_dump())

def convert_tasktemplatelistshowin_to_sdk(src: TasktemplatelistshowIn) -> TaskTemplateListShow:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTemplateListShow(**src.model_dump())
