# Adapter for activitytaskbase
from clio_sdk.models.activitytaskbase import ActivitytaskbaseIn, ActivitytaskbaseOut, ActivitytaskbaseUpdate, ActivitytaskbaseDb
from clio_client.models import activity_task

def convert_sdk_to_activitytaskbaseout(src: activity_task) -> ActivitytaskbaseOut:
    return ActivitytaskbaseOut(**src.dict())

def convert_activitytaskbasein_to_sdk(src: ActivitytaskbaseIn) -> activity_task:
    return activity_task(**src.dict())
