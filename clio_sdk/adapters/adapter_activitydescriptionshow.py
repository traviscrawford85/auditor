# Adapter for activitydescriptionshow
from clio_sdk.models.activitydescriptionshow import ActivitydescriptionshowIn, ActivitydescriptionshowOut, ActivitydescriptionshowUpdate, ActivitydescriptionshowDb
from clio_client.models import activity_description_show

def convert_sdk_to_activitydescriptionshowout(src: activity_description_show) -> ActivitydescriptionshowOut:
    return ActivitydescriptionshowOut(**src.dict())

def convert_activitydescriptionshowin_to_sdk(src: ActivitydescriptionshowIn) -> activity_description_show:
    return activity_description_show(**src.dict())
