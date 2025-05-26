# Adapter for tasktemplatebase
from clio_sdk.models.tasktemplatebase import TasktemplateBaseIn, TasktemplatebaseOut, TasktemplatebaseUpdate, TasktemplatebaseDb
from clio_client.models.task_template import TaskTemplate

def convert_sdk_to_tasktemplatebaseout(src: TaskTemplate) -> TasktemplatebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktemplatebaseOut(**src.model_dump())

def convert_tasktemplatebasein_to_sdk(src: TasktemplateBaseIn) -> TaskTemplate:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTemplate(**src.model_dump())
