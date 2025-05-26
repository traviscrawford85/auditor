# Adapter for cliopaymentspaymentshow
from clio_sdk.models.cliopaymentspaymentshow import CliopaymentspaymentshowIn, CliopaymentspaymentshowOut, CliopaymentspaymentshowUpdate, CliopaymentspaymentshowDb
from clio_client.models import clio_payments_payment_show

def convert_sdk_to_cliopaymentspaymentshowout(src: clio_payments_payment_show) -> CliopaymentspaymentshowOut:
    return CliopaymentspaymentshowOut(**src.dict())

def convert_cliopaymentspaymentshowin_to_sdk(src: CliopaymentspaymentshowIn) -> clio_payments_payment_show:
    return clio_payments_payment_show(**src.dict())
