# Adapter for interestchargelist
from clio_sdk.models.interestchargelist import InterestchargelistIn, InterestchargelistOut, InterestchargelistUpdate, InterestchargelistDb
from clio_client.models import interest_charge_list

def convert_sdk_to_interestchargelistout(src: interest_charge_list) -> InterestchargelistOut:
    return InterestchargelistOut(**src.dict())

def convert_interestchargelistin_to_sdk(src: InterestchargelistIn) -> interest_charge_list:
    return interest_charge_list(**src.dict())
