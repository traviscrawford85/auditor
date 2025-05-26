# Adapter for relationshipbase
from clio_sdk.models.relationshipbase import RelationshipbaseIn, RelationshipbaseOut, RelationshipbaseUpdate, RelationshipbaseDb
from clio_client.models import relationship

def convert_sdk_to_relationshipbaseout(src: relationship) -> RelationshipbaseOut:
    return RelationshipbaseOut(**src.dict())

def convert_relationshipbasein_to_sdk(src: RelationshipbaseIn) -> relationship:
    return relationship(**src.dict())
