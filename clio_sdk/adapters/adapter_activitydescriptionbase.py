# Adapter for activitydescriptionbase
from clio_sdk.models.activitydescriptionbase import ActivitydescriptionbaseIn, ActivitydescriptionbaseOut, ActivitydescriptionbaseUpdate, ActivitydescriptionbaseDb
from clio_client.models import activity_description

def convert_sdk_to_activitydescriptionbaseout(src: activity_description) -> ActivitydescriptionbaseOut:
    return ActivitydescriptionbaseOut(**src.dict())

def convert_activitydescriptionbasein_to_sdk(src: ActivitydescriptionbaseIn) -> activity_description:
    return activity_description(**src.dict())
