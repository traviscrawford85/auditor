# Adapter for tasktemplateshow
from clio_sdk.models.tasktemplateshow import TasktemplateshowIn, TasktemplateshowOut, TasktemplateshowUpdate, TasktemplateshowDb
from clio_client.models.task_template_show import TaskTemplateShow

def convert_sdk_to_tasktemplateshowout(src: TaskTemplateShow) -> TasktemplateshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktemplateshowOut(**src.model_dump())

def convert_tasktemplateshowin_to_sdk(src: TasktemplateshowIn) -> TaskTemplateShow:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTemplateShow(**src.model_dump())
