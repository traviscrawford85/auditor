# Adapter for creditmemoshow
from clio_sdk.models.creditmemoshow import CreditmemoshowIn, CreditmemoshowOut, CreditmemoshowUpdate, CreditmemoshowDb
from clio_client.models.credit_memo_show import CreditMemoShow

def convert_sdk_to_creditmemoshowout(src: CreditMemoShow) -> CreditmemoshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CreditmemoshowOut(**src.model_dump())

def convert_creditmemoshowin_to_sdk(src: CreditmemoshowIn) -> CreditMemoShow:
    """Converts a clio_sdk model to clio_client model."""
    return CreditMemoShow(**src.model_dump())
