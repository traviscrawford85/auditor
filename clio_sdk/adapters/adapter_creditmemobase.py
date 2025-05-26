# Adapter for creditmemobase
from clio_sdk.models.creditmemobase import CreditmemoBaseIn, CreditmemobaseOut, CreditmemobaseUpdate, CreditmemobaseDb
from clio_client.models.credit_memo import CreditMemo

def convert_sdk_to_creditmemobaseout(src: CreditMemo) -> CreditmemobaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CreditmemobaseOut(**src.model_dump())

def convert_creditmemobasein_to_sdk(src: CreditmemoBaseIn) -> CreditMemo:
    """Converts a clio_sdk model to clio_client model."""
    return CreditMemo(**src.model_dump())
