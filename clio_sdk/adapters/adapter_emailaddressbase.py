# Adapter for emailaddressbase
from clio_sdk.models.emailaddressbase import EmailaddressBaseIn, EmailaddressbaseOut, EmailaddressbaseUpdate, EmailaddressbaseDb
from clio_client.models.email_address_base import EmailAddressBase

def convert_sdk_to_emailaddressbaseout(src: EmailAddressBase) -> EmailaddressbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return EmailaddressbaseOut(**src.model_dump())

def convert_emailaddressbasein_to_sdk(src: EmailaddressBaseIn) -> EmailAddressBase:
    """Converts a clio_sdk model to clio_client model."""
    return EmailAddressBase(**src.model_dump())
