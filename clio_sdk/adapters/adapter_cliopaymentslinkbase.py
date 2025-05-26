# Adapter for cliopaymentslinkbase
from clio_sdk.models.cliopaymentslinkbase import CliopaymentslinkbaseIn, CliopaymentslinkbaseOut, CliopaymentslinkbaseUpdate, CliopaymentslinkbaseDb
from clio_client.models import clio_payments_link

def convert_sdk_to_cliopaymentslinkbaseout(src: clio_payments_link) -> CliopaymentslinkbaseOut:
    return CliopaymentslinkbaseOut(**src.dict())

def convert_cliopaymentslinkbasein_to_sdk(src: CliopaymentslinkbaseIn) -> clio_payments_link:
    return clio_payments_link(**src.dict())
