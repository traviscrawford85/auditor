# Adapter for practicearealist
from clio_sdk.models.practicearealist import PracticearealistIn, PracticearealistOut, PracticearealistUpdate, PracticearealistDb
from clio_client.models import practice_area_list

def convert_sdk_to_practicearealistout(src: practice_area_list) -> PracticearealistOut:
    return PracticearealistOut(**src.dict())

def convert_practicearealistin_to_sdk(src: PracticearealistIn) -> practice_area_list:
    return practice_area_list(**src.dict())
