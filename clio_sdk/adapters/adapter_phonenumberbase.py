# Adapter for phonenumberbase
from clio_sdk.models.phonenumberbase import PhonenumberbaseIn, PhonenumberbaseOut, PhonenumberbaseUpdate, PhonenumberbaseDb
from clio_client.models import phone_number_base

def convert_sdk_to_phonenumberbaseout(src: phone_number_base) -> PhonenumberbaseOut:
    return PhonenumberbaseOut(**src.dict())

def convert_phonenumberbasein_to_sdk(src: PhonenumberbaseIn) -> phone_number_base:
    return phone_number_base(**src.dict())
