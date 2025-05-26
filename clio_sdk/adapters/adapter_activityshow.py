# Adapter for activityshow
from clio_sdk.models.activityshow import ActivityshowIn, ActivityshowOut, ActivityshowUpdate, ActivityshowDb
from clio_client.models.activity_show import ActivityShow

def convert_sdk_to_activityshowout(src: ActivityShow) -> ActivityshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivityshowOut(**src.model_dump())

def convert_activityshowin_to_sdk(src: ActivityshowIn) -> ActivityShow:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityShow(**src.model_dump())
