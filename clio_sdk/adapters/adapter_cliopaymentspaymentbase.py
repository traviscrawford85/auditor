# Adapter for cliopaymentspaymentbase
from clio_sdk.models.cliopaymentspaymentbase import CliopaymentspaymentBaseIn, CliopaymentspaymentbaseOut, CliopaymentspaymentbaseUpdate, CliopaymentspaymentbaseDb
from clio_client.models.clio_payments_payment import ClioPaymentsPayment

def convert_sdk_to_cliopaymentspaymentbaseout(src: ClioPaymentsPayment) -> CliopaymentspaymentbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CliopaymentspaymentbaseOut(**src.model_dump())

def convert_cliopaymentspaymentbasein_to_sdk(src: CliopaymentspaymentBaseIn) -> ClioPaymentsPayment:
    """Converts a clio_sdk model to clio_client model."""
    return ClioPaymentsPayment(**src.model_dump())
