# Adapter for phonenumberbase
from clio_sdk.models.phonenumberbase import PhonenumberBaseIn, PhonenumberbaseOut, PhonenumberbaseUpdate, PhonenumberbaseDb
from clio_client.models.phone_number_base import PhoneNumberBase

def convert_sdk_to_phonenumberbaseout(src: PhoneNumberBase) -> PhonenumberbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PhonenumberbaseOut(**src.model_dump())

def convert_phonenumberbasein_to_sdk(src: PhonenumberBaseIn) -> PhoneNumberBase:
    """Converts a clio_sdk model to clio_client model."""
    return PhoneNumberBase(**src.model_dump())
