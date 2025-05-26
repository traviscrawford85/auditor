# Adapter for cliopaymentspaymentbase
from clio_sdk.models.cliopaymentspaymentbase import CliopaymentspaymentbaseIn, CliopaymentspaymentbaseOut, CliopaymentspaymentbaseUpdate, CliopaymentspaymentbaseDb
from clio_client.models import clio_payments_payment

def convert_sdk_to_cliopaymentspaymentbaseout(src: clio_payments_payment) -> CliopaymentspaymentbaseOut:
    return CliopaymentspaymentbaseOut(**src.dict())

def convert_cliopaymentspaymentbasein_to_sdk(src: CliopaymentspaymentbaseIn) -> clio_payments_payment:
    return clio_payments_payment(**src.dict())
