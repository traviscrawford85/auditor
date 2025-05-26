# Adapter for activitydescriptionratebase
from clio_sdk.models.activitydescriptionratebase import ActivitydescriptionrateBaseIn, ActivitydescriptionratebaseOut, ActivitydescriptionratebaseUpdate, ActivitydescriptionratebaseDb
from clio_client.models.activity_description_rate import ActivityDescriptionRate

def convert_sdk_to_activitydescriptionratebaseout(src: ActivityDescriptionRate) -> ActivitydescriptionratebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivitydescriptionratebaseOut(**src.model_dump())

def convert_activitydescriptionratebasein_to_sdk(src: ActivitydescriptionrateBaseIn) -> ActivityDescriptionRate:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityDescriptionRate(**src.model_dump())
