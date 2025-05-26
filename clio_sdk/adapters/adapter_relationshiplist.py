# Adapter for relationshiplist
from clio_sdk.models.relationshiplist import RelationshiplistIn, RelationshiplistOut, RelationshiplistUpdate, RelationshiplistDb
from clio_client.models import relationship_list

def convert_sdk_to_relationshiplistout(src: relationship_list) -> RelationshiplistOut:
    return RelationshiplistOut(**src.dict())

def convert_relationshiplistin_to_sdk(src: RelationshiplistIn) -> relationship_list:
    return relationship_list(**src.dict())
