# Adapter for interestchargelist
from clio_sdk.models.interestchargelist import InterestchargelistIn, InterestchargelistOut, InterestchargelistUpdate, InterestchargelistDb
from clio_client.models.interest_charge_list import InterestChargeList

def convert_sdk_to_interestchargelistout(src: InterestChargeList) -> InterestchargelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return InterestchargelistOut(**src.model_dump())

def convert_interestchargelistin_to_sdk(src: InterestchargelistIn) -> InterestChargeList:
    """Converts a clio_sdk model to clio_client model."""
    return InterestChargeList(**src.model_dump())
