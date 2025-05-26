# Adapter for contingencyfeebase
from clio_sdk.models.contingencyfeebase import ContingencyfeebaseIn, ContingencyfeebaseOut, ContingencyfeebaseUpdate, ContingencyfeebaseDb
from clio_client.models import contingency_fee_base

def convert_sdk_to_contingencyfeebaseout(src: contingency_fee_base) -> ContingencyfeebaseOut:
    return ContingencyfeebaseOut(**src.dict())

def convert_contingencyfeebasein_to_sdk(src: ContingencyfeebaseIn) -> contingency_fee_base:
    return contingency_fee_base(**src.dict())
