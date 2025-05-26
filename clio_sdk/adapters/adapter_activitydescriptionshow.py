# Adapter for activitydescriptionshow
from clio_sdk.models.activitydescriptionshow import ActivitydescriptionshowIn, ActivitydescriptionshowOut, ActivitydescriptionshowUpdate, ActivitydescriptionshowDb
from clio_client.models.activity_description_show import ActivityDescriptionShow

def convert_sdk_to_activitydescriptionshowout(src: ActivityDescriptionShow) -> ActivitydescriptionshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitydescriptionshowOut(**src.model_dump())

def convert_activitydescriptionshowin_to_sdk(src: ActivitydescriptionshowIn) -> ActivityDescriptionShow:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityDescriptionShow(**src.model_dump())
