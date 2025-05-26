# Adapter for cliopaymentspaymentlist
from clio_sdk.models.cliopaymentspaymentlist import CliopaymentspaymentlistIn, CliopaymentspaymentlistOut, CliopaymentspaymentlistUpdate, CliopaymentspaymentlistDb
from clio_client.models.clio_payments_payment_list import ClioPaymentsPaymentList

def convert_sdk_to_cliopaymentspaymentlistout(src: ClioPaymentsPaymentList) -> CliopaymentspaymentlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CliopaymentspaymentlistOut(**src.model_dump())

def convert_cliopaymentspaymentlistin_to_sdk(src: CliopaymentspaymentlistIn) -> ClioPaymentsPaymentList:
    """Converts a clio_sdk model to clio_client model."""
    return ClioPaymentsPaymentList(**src.model_dump())
