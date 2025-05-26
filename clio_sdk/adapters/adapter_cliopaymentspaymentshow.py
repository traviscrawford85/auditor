# Adapter for cliopaymentspaymentshow
from clio_sdk.models.cliopaymentspaymentshow import CliopaymentspaymentshowIn, CliopaymentspaymentshowOut, CliopaymentspaymentshowUpdate, CliopaymentspaymentshowDb
from clio_client.models.clio_payments_payment_show import ClioPaymentsPaymentShow

def convert_sdk_to_cliopaymentspaymentshowout(src: ClioPaymentsPaymentShow) -> CliopaymentspaymentshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CliopaymentspaymentshowOut(**src.model_dump())

def convert_cliopaymentspaymentshowin_to_sdk(src: CliopaymentspaymentshowIn) -> ClioPaymentsPaymentShow:
    """Converts a clio_sdk model to clio_client model."""
    return ClioPaymentsPaymentShow(**src.model_dump())
