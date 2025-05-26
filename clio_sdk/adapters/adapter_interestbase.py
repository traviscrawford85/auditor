# Adapter for interestbase
from clio_sdk.models.interestbase import InterestbaseIn, InterestbaseOut, InterestbaseUpdate, InterestbaseDb
from clio_client.models import interest_base

def convert_sdk_to_interestbaseout(src: interest_base) -> InterestbaseOut:
    return InterestbaseOut(**src.dict())

def convert_interestbasein_to_sdk(src: InterestbaseIn) -> interest_base:
    return interest_base(**src.dict())
