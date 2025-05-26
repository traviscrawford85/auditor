# Adapter for tasktemplateshow
from clio_sdk.models.tasktemplateshow import TasktemplateshowIn, TasktemplateshowOut, TasktemplateshowUpdate, TasktemplateshowDb
from clio_client.models import task_template_show

def convert_sdk_to_tasktemplateshowout(src: task_template_show) -> TasktemplateshowOut:
    return TasktemplateshowOut(**src.dict())

def convert_tasktemplateshowin_to_sdk(src: TasktemplateshowIn) -> task_template_show:
    return task_template_show(**src.dict())
