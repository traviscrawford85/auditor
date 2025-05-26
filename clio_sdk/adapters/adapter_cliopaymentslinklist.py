# Adapter for cliopaymentslinklist
from clio_sdk.models.cliopaymentslinklist import CliopaymentslinklistIn, CliopaymentslinklistOut, CliopaymentslinklistUpdate, CliopaymentslinklistDb
from clio_client.models import clio_payments_link_list

def convert_sdk_to_cliopaymentslinklistout(src: clio_payments_link_list) -> CliopaymentslinklistOut:
    return CliopaymentslinklistOut(**src.dict())

def convert_cliopaymentslinklistin_to_sdk(src: CliopaymentslinklistIn) -> clio_payments_link_list:
    return clio_payments_link_list(**src.dict())
