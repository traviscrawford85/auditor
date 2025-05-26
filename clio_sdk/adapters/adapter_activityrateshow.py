# Adapter for activityrateshow
from clio_sdk.models.activityrateshow import ActivityrateshowIn, ActivityrateshowOut, ActivityrateshowUpdate, ActivityrateshowDb
from clio_client.models.activity_rate_show import ActivityRateShow

def convert_sdk_to_activityrateshowout(src: ActivityRateShow) -> ActivityrateshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ActivityrateshowOut(**src.model_dump())

def convert_activityrateshowin_to_sdk(src: ActivityrateshowIn) -> ActivityRateShow:
    """Converts a clio_sdk model to clio_client model."""
    return ActivityRateShow(**src.model_dump())
