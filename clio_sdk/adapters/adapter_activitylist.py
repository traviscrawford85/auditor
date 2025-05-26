# Adapter for activitylist
from clio_sdk.models.activitylist import ActivitylistIn, ActivitylistOut, ActivitylistUpdate, ActivitylistDb
from clio_client.models import activity_list

def convert_sdk_to_activitylistout(src: activity_list) -> ActivitylistOut:
    return ActivitylistOut(**src.dict())

def convert_activitylistin_to_sdk(src: ActivitylistIn) -> activity_list:
    return activity_list(**src.dict())
