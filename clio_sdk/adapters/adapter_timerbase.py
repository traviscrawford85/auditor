# Adapter for timerbase
from clio_sdk.models.timerbase import TimerbaseIn, TimerbaseOut, TimerbaseUpdate, TimerbaseDb
from clio_client.models import timer

def convert_sdk_to_timerbaseout(src: timer) -> TimerbaseOut:
    return TimerbaseOut(**src.dict())

def convert_timerbasein_to_sdk(src: TimerbaseIn) -> timer:
    return timer(**src.dict())
