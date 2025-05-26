# Adapter for activityshow
from clio_sdk.models.activityshow import ActivityshowIn, ActivityshowOut, ActivityshowUpdate, ActivityshowDb
from clio_client.models import activity_show

def convert_sdk_to_activityshowout(src: activity_show) -> ActivityshowOut:
    return ActivityshowOut(**src.dict())

def convert_activityshowin_to_sdk(src: ActivityshowIn) -> activity_show:
    return activity_show(**src.dict())
