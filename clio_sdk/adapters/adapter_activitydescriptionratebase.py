# Adapter for activitydescriptionratebase
from clio_sdk.models.activitydescriptionratebase import ActivitydescriptionratebaseIn, ActivitydescriptionratebaseOut, ActivitydescriptionratebaseUpdate, ActivitydescriptionratebaseDb
from clio_client.models import activity_description_rate

def convert_sdk_to_activitydescriptionratebaseout(src: activity_description_rate) -> ActivitydescriptionratebaseOut:
    return ActivitydescriptionratebaseOut(**src.dict())

def convert_activitydescriptionratebasein_to_sdk(src: ActivitydescriptionratebaseIn) -> activity_description_rate:
    return activity_description_rate(**src.dict())
