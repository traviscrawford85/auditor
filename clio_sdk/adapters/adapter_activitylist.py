# Adapter for activitylist
from clio_sdk.models.activitylist import ActivitylistIn, ActivitylistOut, ActivitylistUpdate, ActivitylistDb
from clio_client.models.activity_list import ActivityList

def convert_sdk_to_activitylistout(src: ActivityList) -> ActivitylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitylistOut(**src.model_dump())

def convert_activitylistin_to_sdk(src: ActivitylistIn) -> ActivityList:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityList(**src.model_dump())
