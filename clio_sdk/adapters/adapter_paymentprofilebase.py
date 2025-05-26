# Adapter for paymentprofilebase
from clio_sdk.models.paymentprofilebase import PaymentprofilebaseIn, PaymentprofilebaseOut, PaymentprofilebaseUpdate, PaymentprofilebaseDb
from clio_client.models import payment_profile_base

def convert_sdk_to_paymentprofilebaseout(src: payment_profile_base) -> PaymentprofilebaseOut:
    return PaymentprofilebaseOut(**src.dict())

def convert_paymentprofilebasein_to_sdk(src: PaymentprofilebaseIn) -> payment_profile_base:
    return payment_profile_base(**src.dict())
