# Adapter for contactlist
from clio_sdk.models.contactlist import ContactlistIn, ContactlistOut, ContactlistUpdate, ContactlistDb
from clio_client.models import contact_list

def convert_sdk_to_contactlistout(src: contact_list) -> ContactlistOut:
    return ContactlistOut(**src.dict())

def convert_contactlistin_to_sdk(src: ContactlistIn) -> contact_list:
    return contact_list(**src.dict())
