# Adapter for activityratebase
from clio_sdk.models.activityratebase import ActivityratebaseIn, ActivityratebaseOut, ActivityratebaseUpdate, ActivityratebaseDb
from clio_client.models import activity_rate

def convert_sdk_to_activityratebaseout(src: activity_rate) -> ActivityratebaseOut:
    return ActivityratebaseOut(**src.dict())

def convert_activityratebasein_to_sdk(src: ActivityratebaseIn) -> activity_rate:
    return activity_rate(**src.dict())
