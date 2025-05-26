# Adapter for activityratelist
from clio_sdk.models.activityratelist import ActivityratelistIn, ActivityratelistOut, ActivityratelistUpdate, ActivityratelistDb
from clio_client.models.activity_rate_list import ActivityRateList

def convert_sdk_to_activityratelistout(src: ActivityRateList) -> ActivityratelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivityratelistOut(**src.model_dump())

def convert_activityratelistin_to_sdk(src: ActivityratelistIn) -> ActivityRateList:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityRateList(**src.model_dump())
