# Adapter for activityrateshow
from clio_sdk.models.activityrateshow import ActivityrateshowIn, ActivityrateshowOut, ActivityrateshowUpdate, ActivityrateshowDb
from clio_client.models import activity_rate_show

def convert_sdk_to_activityrateshowout(src: activity_rate_show) -> ActivityrateshowOut:
    return ActivityrateshowOut(**src.dict())

def convert_activityrateshowin_to_sdk(src: ActivityrateshowIn) -> activity_rate_show:
    return activity_rate_show(**src.dict())
