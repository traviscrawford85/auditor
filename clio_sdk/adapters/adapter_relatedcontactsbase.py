# Adapter for relatedcontactsbase
from clio_sdk.models.relatedcontactsbase import RelatedcontactsBaseIn, RelatedcontactsbaseOut, RelatedcontactsbaseUpdate, RelatedcontactsbaseDb
from clio_client.models.related_contacts import RelatedContacts

def convert_sdk_to_relatedcontactsbaseout(src: RelatedContacts) -> RelatedcontactsbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return RelatedcontactsbaseOut(**src.model_dump())

def convert_relatedcontactsbasein_to_sdk(src: RelatedcontactsBaseIn) -> RelatedContacts:
    """Converts a clio_sdk model to clio_client model."""
    return RelatedContacts(**src.model_dump())
