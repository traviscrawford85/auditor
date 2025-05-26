# Adapter for relatedcontactslist
from clio_sdk.models.relatedcontactslist import RelatedcontactslistIn, RelatedcontactslistOut, RelatedcontactslistUpdate, RelatedcontactslistDb
from clio_client.models import related_contacts_list

def convert_sdk_to_relatedcontactslistout(src: related_contacts_list) -> RelatedcontactslistOut:
    return RelatedcontactslistOut(**src.dict())

def convert_relatedcontactslistin_to_sdk(src: RelatedcontactslistIn) -> related_contacts_list:
    return related_contacts_list(**src.dict())
