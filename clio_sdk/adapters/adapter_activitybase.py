# Adapter for activitybase
from clio_sdk.models.activitybase import ActivityBaseIn, ActivityBaseOut, ActivityBaseUpdate, ActivityBaseDb
from clio_client.models import activity

def convert_sdk_to_activitybaseout(src: activity) -> ActivitybaseOut:
    return ActivitybaseOut(**src.dict())

def convert_activitybasein_to_sdk(src: ActivitybaseIn) -> activity:
    return activity(**src.dict())
