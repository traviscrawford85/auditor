# Adapter for interestchargebase
from clio_sdk.models.interestchargebase import InterestchargeBaseIn, InterestchargebaseOut, InterestchargebaseUpdate, InterestchargebaseDb
from clio_client.models.interest_charge import InterestCharge

def convert_sdk_to_interestchargebaseout(src: InterestCharge) -> InterestchargebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return InterestchargebaseOut(**src.model_dump())

def convert_interestchargebasein_to_sdk(src: InterestchargeBaseIn) -> InterestCharge:
    """Converts a clio_sdk model to clio_client model."""
    return InterestCharge(**src.model_dump())
