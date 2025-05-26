# Adapter for addressbase
from clio_sdk.models.addressbase import AddressBaseIn, AddressbaseOut, AddressbaseUpdate, AddressbaseDb
from clio_client.models.address_base import AddressBase

def convert_sdk_to_addressbaseout(src: AddressBase) -> AddressbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return AddressbaseOut(**src.model_dump())

def convert_addressbasein_to_sdk(src: AddressBaseIn) -> AddressBase:
    """Converts a clio_sdk model to clio_client model."""
    return AddressBase(**src.model_dump())
