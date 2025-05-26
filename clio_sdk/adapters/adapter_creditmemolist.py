# Adapter for creditmemolist
from clio_sdk.models.creditmemolist import CreditmemolistIn, CreditmemolistOut, CreditmemolistUpdate, CreditmemolistDb
from clio_client.models import credit_memo_list

def convert_sdk_to_creditmemolistout(src: credit_memo_list) -> CreditmemolistOut:
    return CreditmemolistOut(**src.dict())

def convert_creditmemolistin_to_sdk(src: CreditmemolistIn) -> credit_memo_list:
    return credit_memo_list(**src.dict())
