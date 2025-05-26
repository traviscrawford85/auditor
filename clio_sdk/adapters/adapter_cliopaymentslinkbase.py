# Adapter for cliopaymentslinkbase
from clio_sdk.models.cliopaymentslinkbase import CliopaymentslinkBaseIn, CliopaymentslinkbaseOut, CliopaymentslinkbaseUpdate, CliopaymentslinkbaseDb
from clio_client.models.clio_payments_link import ClioPaymentsLink

def convert_sdk_to_cliopaymentslinkbaseout(src: ClioPaymentsLink) -> CliopaymentslinkbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CliopaymentslinkbaseOut(**src.model_dump())

def convert_cliopaymentslinkbasein_to_sdk(src: CliopaymentslinkBaseIn) -> ClioPaymentsLink:
    """Converts a clio_sdk model to clio_client model."""
    return ClioPaymentsLink(**src.model_dump())
