# Adapter for creditmemoshow
from clio_sdk.models.creditmemoshow import CreditmemoshowIn, CreditmemoshowOut, CreditmemoshowUpdate, CreditmemoshowDb
from clio_client.models import credit_memo_show

def convert_sdk_to_creditmemoshowout(src: credit_memo_show) -> CreditmemoshowOut:
    return CreditmemoshowOut(**src.dict())

def convert_creditmemoshowin_to_sdk(src: CreditmemoshowIn) -> credit_memo_show:
    return credit_memo_show(**src.dict())
