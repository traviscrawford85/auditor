# Adapter for contactshow
from clio_sdk.models.contactshow import ContactshowIn, ContactshowOut, ContactshowUpdate, ContactshowDb
from clio_client.models.contact_show import ContactShow

def convert_sdk_to_contactshowout(src: ContactShow) -> ContactshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ContactshowOut(**src.model_dump())

def convert_contactshowin_to_sdk(src: ContactshowIn) -> ContactShow:
    """Converts a clio_sdk model to clio_client model."""
    return ContactShow(**src.model_dump())
