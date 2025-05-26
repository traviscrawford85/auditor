# Adapter for contactbase
from clio_sdk.models.contactbase import ContactbaseIn, ContactbaseOut, ContactbaseUpdate, ContactbaseDb
from clio_client.models import contact

def convert_sdk_to_contactbaseout(src: contact) -> ContactbaseOut:
    return ContactbaseOut(**src.dict())

def convert_contactbasein_to_sdk(src: ContactbaseIn) -> contact:
    return contact(**src.dict())
