# Adapter for contactshow
from clio_sdk.models.contactshow import ContactshowIn, ContactshowOut, ContactshowUpdate, ContactshowDb
from clio_client.models import contact_show

def convert_sdk_to_contactshowout(src: contact_show) -> ContactshowOut:
    return ContactshowOut(**src.dict())

def convert_contactshowin_to_sdk(src: ContactshowIn) -> contact_show:
    return contact_show(**src.dict())
