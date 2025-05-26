# Adapter for tasktemplatelistshow
from clio_sdk.models.tasktemplatelistshow import TasktemplatelistshowIn, TasktemplatelistshowOut, TasktemplatelistshowUpdate, TasktemplatelistshowDb
from clio_client.models import task_template_list_show

def convert_sdk_to_tasktemplatelistshowout(src: task_template_list_show) -> TasktemplatelistshowOut:
    return TasktemplatelistshowOut(**src.dict())

def convert_tasktemplatelistshowin_to_sdk(src: TasktemplatelistshowIn) -> task_template_list_show:
    return task_template_list_show(**src.dict())
