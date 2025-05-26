# Adapter for cliopaymentslinkshow
from clio_sdk.models.cliopaymentslinkshow import CliopaymentslinkshowIn, CliopaymentslinkshowOut, CliopaymentslinkshowUpdate, CliopaymentslinkshowDb
from clio_client.models.clio_payments_link_show import ClioPaymentsLinkShow

def convert_sdk_to_cliopaymentslinkshowout(src: ClioPaymentsLinkShow) -> CliopaymentslinkshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CliopaymentslinkshowOut(**src.model_dump())

def convert_cliopaymentslinkshowin_to_sdk(src: CliopaymentslinkshowIn) -> ClioPaymentsLinkShow:
    """Converts a clio_sdk model to clio_client model."""
    return ClioPaymentsLinkShow(**src.model_dump())
