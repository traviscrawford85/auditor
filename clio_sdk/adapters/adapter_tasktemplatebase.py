# Adapter for tasktemplatebase
from clio_sdk.models.tasktemplatebase import TasktemplatebaseIn, TasktemplatebaseOut, TasktemplatebaseUpdate, TasktemplatebaseDb
from clio_client.models import task_template

def convert_sdk_to_tasktemplatebaseout(src: task_template) -> TasktemplatebaseOut:
    return TasktemplatebaseOut(**src.dict())

def convert_tasktemplatebasein_to_sdk(src: TasktemplatebaseIn) -> task_template:
    return task_template(**src.dict())
