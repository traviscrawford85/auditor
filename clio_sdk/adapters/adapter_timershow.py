# Adapter for timershow
from clio_sdk.models.timershow import TimershowIn, TimershowOut, TimershowUpdate, TimershowDb
from clio_client.models import timer_show

def convert_sdk_to_timershowout(src: timer_show) -> TimershowOut:
    return TimershowOut(**src.dict())

def convert_timershowin_to_sdk(src: TimershowIn) -> timer_show:
    return timer_show(**src.dict())
