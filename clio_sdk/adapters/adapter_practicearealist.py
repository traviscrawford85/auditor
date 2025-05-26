# Adapter for practicearealist
from clio_sdk.models.practicearealist import PracticearealistIn, PracticearealistOut, PracticearealistUpdate, PracticearealistDb
from clio_client.models.practice_area_list import PracticeAreaList

def convert_sdk_to_practicearealistout(src: PracticeAreaList) -> PracticearealistOut:
    """Converts a clio_client model to clio_sdk model."""
    return PracticearealistOut(**src.model_dump())

def convert_practicearealistin_to_sdk(src: PracticearealistIn) -> PracticeAreaList:
    """Converts a clio_sdk model to clio_client model."""
    return PracticeAreaList(**src.model_dump())
