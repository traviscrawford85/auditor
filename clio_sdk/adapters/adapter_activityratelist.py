# Adapter for activityratelist
from clio_sdk.models.activityratelist import ActivityratelistIn, ActivityratelistOut, ActivityratelistUpdate, ActivityratelistDb
from clio_client.models import activity_rate_list

def convert_sdk_to_activityratelistout(src: activity_rate_list) -> ActivityratelistOut:
    return ActivityratelistOut(**src.dict())

def convert_activityratelistin_to_sdk(src: ActivityratelistIn) -> activity_rate_list:
    return activity_rate_list(**src.dict())
