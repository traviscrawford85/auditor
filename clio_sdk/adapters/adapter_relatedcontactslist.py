# Adapter for relatedcontactslist
from clio_sdk.models.relatedcontactslist import RelatedcontactslistIn, RelatedcontactslistOut, RelatedcontactslistUpdate, RelatedcontactslistDb
from clio_client.models.related_contacts_list import RelatedContactsList

def convert_sdk_to_relatedcontactslistout(src: RelatedContactsList) -> RelatedcontactslistOut:
    """Converts a clio_client model to clio_sdk model."""
    return RelatedcontactslistOut(**src.model_dump())

def convert_relatedcontactslistin_to_sdk(src: RelatedcontactslistIn) -> RelatedContactsList:
    """Converts a clio_sdk model to clio_client model."""
    return RelatedContactsList(**src.model_dump())
