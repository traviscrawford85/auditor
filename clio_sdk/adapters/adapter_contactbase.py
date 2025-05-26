# Adapter for contactbase
from clio_sdk.models.contactbase import ContactBaseIn, ContactbaseOut, ContactbaseUpdate, ContactbaseDb
from clio_client.models.contact import Contact

def convert_sdk_to_contactbaseout(src: Contact) -> ContactbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ContactbaseOut(**src.model_dump())

def convert_contactbasein_to_sdk(src: ContactBaseIn) -> Contact:
    """Converts a clio_sdk model to clio_client model."""
    return Contact(**src.model_dump())
