# Adapter for interestbase
from clio_sdk.models.interestbase import InterestBaseIn, InterestbaseOut, InterestbaseUpdate, InterestbaseDb
from clio_client.models.interest_base import InterestBase

def convert_sdk_to_interestbaseout(src: InterestBase) -> InterestbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return InterestbaseOut(**src.model_dump())

def convert_interestbasein_to_sdk(src: InterestBaseIn) -> InterestBase:
    """Converts a clio_sdk model to clio_client model."""
    return InterestBase(**src.model_dump())
