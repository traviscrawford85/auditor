# Adapter for activitybase
from clio_sdk.models.activitybase import ActivityBaseIn, ActivitybaseOut, ActivitybaseUpdate, ActivitybaseDb
from clio_client.models.activity import Activity

def convert_sdk_to_activitybaseout(src: Activity) -> ActivitybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitybaseOut(**src.model_dump())

def convert_activitybasein_to_sdk(src: ActivityBaseIn) -> Activity:
    """Converts a clio_sdk model to clio_client model."""
    return Activity(**src.model_dump())
