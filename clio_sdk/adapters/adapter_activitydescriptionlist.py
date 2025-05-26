# Adapter for activitydescriptionlist
from clio_sdk.models.activitydescriptionlist import ActivitydescriptionlistIn, ActivitydescriptionlistOut, ActivitydescriptionlistUpdate, ActivitydescriptionlistDb
from clio_client.models.activity_description_list import ActivityDescriptionList

def convert_sdk_to_activitydescriptionlistout(src: ActivityDescriptionList) -> ActivitydescriptionlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitydescriptionlistOut(**src.model_dump())

def convert_activitydescriptionlistin_to_sdk(src: ActivitydescriptionlistIn) -> ActivityDescriptionList:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityDescriptionList(**src.model_dump())
