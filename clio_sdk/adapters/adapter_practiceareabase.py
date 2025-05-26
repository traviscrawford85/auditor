# Adapter for practiceareabase
from clio_sdk.models.practiceareabase import PracticeareaBaseIn, PracticeareabaseOut, PracticeareabaseUpdate, PracticeareabaseDb
from clio_client.models.practice_area import PracticeArea

def convert_sdk_to_practiceareabaseout(src: PracticeArea) -> PracticeareabaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PracticeareabaseOut(**src.model_dump())

def convert_practiceareabasein_to_sdk(src: PracticeareaBaseIn) -> PracticeArea:
    """Converts a clio_sdk model to clio_client model."""
    return PracticeArea(**src.model_dump())
