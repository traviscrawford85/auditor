# Adapter for paymentprofilebase
from clio_sdk.models.paymentprofilebase import PaymentprofileBaseIn, PaymentprofilebaseOut, PaymentprofilebaseUpdate, PaymentprofilebaseDb
from clio_client.models.payment_profile_base import PaymentProfileBase

def convert_sdk_to_paymentprofilebaseout(src: PaymentProfileBase) -> PaymentprofilebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PaymentprofilebaseOut(**src.model_dump())

def convert_paymentprofilebasein_to_sdk(src: PaymentprofileBaseIn) -> PaymentProfileBase:
    """Converts a clio_sdk model to clio_client model."""
    return PaymentProfileBase(**src.model_dump())
