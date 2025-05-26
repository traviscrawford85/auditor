# Adapter for interestchargebase
from clio_sdk.models.interestchargebase import InterestchargebaseIn, InterestchargebaseOut, InterestchargebaseUpdate, InterestchargebaseDb
from clio_client.models import interest_charge

def convert_sdk_to_interestchargebaseout(src: interest_charge) -> InterestchargebaseOut:
    return InterestchargebaseOut(**src.dict())

def convert_interestchargebasein_to_sdk(src: InterestchargebaseIn) -> interest_charge:
    return interest_charge(**src.dict())
