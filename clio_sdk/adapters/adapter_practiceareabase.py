# Adapter for practiceareabase
from clio_sdk.models.practiceareabase import PracticeareabaseIn, PracticeareabaseOut, PracticeareabaseUpdate, PracticeareabaseDb
from clio_client.models import practice_area

def convert_sdk_to_practiceareabaseout(src: practice_area) -> PracticeareabaseOut:
    return PracticeareabaseOut(**src.dict())

def convert_practiceareabasein_to_sdk(src: PracticeareabaseIn) -> practice_area:
    return practice_area(**src.dict())
