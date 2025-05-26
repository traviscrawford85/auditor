# Adapter for timershow
from clio_sdk.models.timershow import TimershowIn, TimershowOut, TimershowUpdate, TimershowDb
from clio_client.models.timer_show import TimerShow

def convert_sdk_to_timershowout(src: TimerShow) -> TimershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TimershowOut(**src.model_dump())

def convert_timershowin_to_sdk(src: TimershowIn) -> TimerShow:
    """Converts a clio_sdk model to clio_client model."""
    return TimerShow(**src.model_dump())
