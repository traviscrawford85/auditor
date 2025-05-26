# Adapter for activityratebase
from clio_sdk.models.activityratebase import ActivityrateBaseIn, ActivityratebaseOut, ActivityratebaseUpdate, ActivityratebaseDb
from clio_client.models.activity_rate import ActivityRate

def convert_sdk_to_activityratebaseout(src: ActivityRate) -> ActivityratebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivityratebaseOut(**src.model_dump())

def convert_activityratebasein_to_sdk(src: ActivityrateBaseIn) -> ActivityRate:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityRate(**src.model_dump())
