# Adapter for timerbase
from clio_sdk.models.timerbase import TimerBaseIn, TimerbaseOut, TimerbaseUpdate, TimerbaseDb
from clio_client.models.timer import Timer

def convert_sdk_to_timerbaseout(src: Timer) -> TimerbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TimerbaseOut(**src.model_dump())

def convert_timerbasein_to_sdk(src: TimerBaseIn) -> Timer:
    """Converts a clio_sdk model to clio_client model."""
    return Timer(**src.model_dump())
