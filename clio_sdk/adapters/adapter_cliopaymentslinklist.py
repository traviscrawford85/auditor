# Adapter for cliopaymentslinklist
from clio_sdk.models.cliopaymentslinklist import CliopaymentslinklistIn, CliopaymentslinklistOut, CliopaymentslinklistUpdate, CliopaymentslinklistDb
from clio_client.models.clio_payments_link_list import ClioPaymentsLinkList

def convert_sdk_to_cliopaymentslinklistout(src: ClioPaymentsLinkList) -> CliopaymentslinklistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CliopaymentslinklistOut(**src.model_dump())

def convert_cliopaymentslinklistin_to_sdk(src: CliopaymentslinklistIn) -> ClioPaymentsLinkList:
    """Converts a clio_sdk model to clio_client model."""
    return ClioPaymentsLinkList(**src.model_dump())
