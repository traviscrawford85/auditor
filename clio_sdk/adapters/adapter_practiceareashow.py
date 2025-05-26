# Adapter for practiceareashow
from clio_sdk.models.practiceareashow import PracticeareashowIn, PracticeareashowOut, PracticeareashowUpdate, PracticeareashowDb
from clio_client.models import practice_area_show

def convert_sdk_to_practiceareashowout(src: practice_area_show) -> PracticeareashowOut:
    return PracticeareashowOut(**src.dict())

def convert_practiceareashowin_to_sdk(src: PracticeareashowIn) -> practice_area_show:
    return practice_area_show(**src.dict())
