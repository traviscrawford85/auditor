# Adapter for relatedcontactsbase
from clio_sdk.models.relatedcontactsbase import RelatedcontactsbaseIn, RelatedcontactsbaseOut, RelatedcontactsbaseUpdate, RelatedcontactsbaseDb
from clio_client.models import related_contacts

def convert_sdk_to_relatedcontactsbaseout(src: related_contacts) -> RelatedcontactsbaseOut:
    return RelatedcontactsbaseOut(**src.dict())

def convert_relatedcontactsbasein_to_sdk(src: RelatedcontactsbaseIn) -> related_contacts:
    return related_contacts(**src.dict())
