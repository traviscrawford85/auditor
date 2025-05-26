# Adapter for practiceareashow
from clio_sdk.models.practiceareashow import PracticeareashowIn, PracticeareashowOut, PracticeareashowUpdate, PracticeareashowDb
from clio_client.models.practice_area_show import PracticeAreaShow

def convert_sdk_to_practiceareashowout(src: PracticeAreaShow) -> PracticeareashowOut:
    """Converts a clio_client model to clio_sdk model."""
    return PracticeareashowOut(**src.model_dump())

def convert_practiceareashowin_to_sdk(src: PracticeareashowIn) -> PracticeAreaShow:
    """Converts a clio_sdk model to clio_client model."""
    return PracticeAreaShow(**src.model_dump())
