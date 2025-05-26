# Adapter for addressbase
from clio_sdk.models.addressbase import AddressbaseIn, AddressbaseOut, AddressbaseUpdate, AddressbaseDb
from clio_client.models import address_base

def convert_sdk_to_addressbaseout(src: address_base) -> AddressbaseOut:
    return AddressbaseOut(**src.dict())

def convert_addressbasein_to_sdk(src: AddressbaseIn) -> address_base:
    return address_base(**src.dict())
