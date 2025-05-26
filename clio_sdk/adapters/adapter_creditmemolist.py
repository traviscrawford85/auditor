# Adapter for creditmemolist
from clio_sdk.models.creditmemolist import CreditmemolistIn, CreditmemolistOut, CreditmemolistUpdate, CreditmemolistDb
from clio_client.models.credit_memo_list import CreditMemoList

def convert_sdk_to_creditmemolistout(src: CreditMemoList) -> CreditmemolistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CreditmemolistOut(**src.model_dump())

def convert_creditmemolistin_to_sdk(src: CreditmemolistIn) -> CreditMemoList:
    """Converts a clio_sdk model to clio_client model."""
    return CreditMemoList(**src.model_dump())
