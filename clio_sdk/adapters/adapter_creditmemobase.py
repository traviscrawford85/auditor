# Adapter for creditmemobase
from clio_sdk.models.creditmemobase import CreditmemobaseIn, CreditmemobaseOut, CreditmemobaseUpdate, CreditmemobaseDb
from clio_client.models import credit_memo

def convert_sdk_to_creditmemobaseout(src: credit_memo) -> CreditmemobaseOut:
    return CreditmemobaseOut(**src.dict())

def convert_creditmemobasein_to_sdk(src: CreditmemobaseIn) -> credit_memo:
    return credit_memo(**src.dict())
