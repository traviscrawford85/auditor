# Adapter for cliopaymentspaymentlist
from clio_sdk.models.cliopaymentspaymentlist import CliopaymentspaymentlistIn, CliopaymentspaymentlistOut, CliopaymentspaymentlistUpdate, CliopaymentspaymentlistDb
from clio_client.models import clio_payments_payment_list

def convert_sdk_to_cliopaymentspaymentlistout(src: clio_payments_payment_list) -> CliopaymentspaymentlistOut:
    return CliopaymentspaymentlistOut(**src.dict())

def convert_cliopaymentspaymentlistin_to_sdk(src: CliopaymentspaymentlistIn) -> clio_payments_payment_list:
    return clio_payments_payment_list(**src.dict())
