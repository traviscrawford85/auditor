# Adapter for activitytaskbase
from clio_sdk.models.activitytaskbase import ActivitytaskBaseIn, ActivitytaskbaseOut, ActivitytaskbaseUpdate, ActivitytaskbaseDb
from clio_client.models.activity_task import ActivityTask

def convert_sdk_to_activitytaskbaseout(src: ActivityTask) -> ActivitytaskbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitytaskbaseOut(**src.model_dump())

def convert_activitytaskbasein_to_sdk(src: ActivitytaskBaseIn) -> ActivityTask:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityTask(**src.model_dump())
