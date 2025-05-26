# Adapter for cliopaymentslinkshow
from clio_sdk.models.cliopaymentslinkshow import CliopaymentslinkshowIn, CliopaymentslinkshowOut, CliopaymentslinkshowUpdate, CliopaymentslinkshowDb
from clio_client.models import clio_payments_link_show

def convert_sdk_to_cliopaymentslinkshowout(src: clio_payments_link_show) -> CliopaymentslinkshowOut:
    return CliopaymentslinkshowOut(**src.dict())

def convert_cliopaymentslinkshowin_to_sdk(src: CliopaymentslinkshowIn) -> clio_payments_link_show:
    return clio_payments_link_show(**src.dict())
