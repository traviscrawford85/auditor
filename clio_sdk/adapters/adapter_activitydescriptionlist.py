# Adapter for activitydescriptionlist
from clio_sdk.models.activitydescriptionlist import ActivitydescriptionlistIn, ActivitydescriptionlistOut, ActivitydescriptionlistUpdate, ActivitydescriptionlistDb
from clio_client.models import activity_description_list

def convert_sdk_to_activitydescriptionlistout(src: activity_description_list) -> ActivitydescriptionlistOut:
    return ActivitydescriptionlistOut(**src.dict())

def convert_activitydescriptionlistin_to_sdk(src: ActivitydescriptionlistIn) -> activity_description_list:
    return activity_description_list(**src.dict())
