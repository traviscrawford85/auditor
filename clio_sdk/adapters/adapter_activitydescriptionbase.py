# Adapter for activitydescriptionbase
from clio_sdk.models.activitydescriptionbase import ActivitydescriptionBaseIn, ActivitydescriptionbaseOut, ActivitydescriptionbaseUpdate, ActivitydescriptionbaseDb
from clio_client.models.activity_description import ActivityDescription

def convert_sdk_to_activitydescriptionbaseout(src: ActivityDescription) -> ActivitydescriptionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitydescriptionbaseOut(**src.model_dump())

def convert_activitydescriptionbasein_to_sdk(src: ActivitydescriptionBaseIn) -> ActivityDescription:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityDescription(**src.model_dump())
