# Adapter for contactlist
from clio_sdk.models.contactlist import ContactlistIn, ContactlistOut, ContactlistUpdate, ContactlistDb
from clio_client.models.contact_list import ContactList

def convert_sdk_to_contactlistout(src: ContactList) -> ContactlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ContactlistOut(**src.model_dump())

def convert_contactlistin_to_sdk(src: ContactlistIn) -> ContactList:
    """Converts a clio_sdk model to clio_client model."""
    return ContactList(**src.model_dump())
