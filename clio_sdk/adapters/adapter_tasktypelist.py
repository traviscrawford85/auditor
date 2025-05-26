# Adapter for tasktypelist
from clio_sdk.models.tasktypelist import TasktypelistIn, TasktypelistOut, TasktypelistUpdate, TasktypelistDb
from clio_client.models.task_type_list import TaskTypeList

def convert_sdk_to_tasktypelistout(src: TaskTypeList) -> TasktypelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return TasktypelistOut(**src.model_dump())

def convert_tasktypelistin_to_sdk(src: TasktypelistIn) -> TaskTypeList:
    """Converts a clio_sdk model to clio_client model."""
    return TaskTypeList(**src.model_dump())
