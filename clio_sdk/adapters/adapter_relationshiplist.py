# Adapter for relationshiplist
from clio_sdk.models.relationshiplist import RelationshiplistIn, RelationshiplistOut, RelationshiplistUpdate, RelationshiplistDb
from clio_client.models.relationship_list import RelationshipList

def convert_sdk_to_relationshiplistout(src: RelationshipList) -> RelationshiplistOut:
    """Converts a clio_client model to clio_sdk model."""
    return RelationshiplistOut(**src.model_dump())

def convert_relationshiplistin_to_sdk(src: RelationshiplistIn) -> RelationshipList:
    """Converts a clio_sdk model to clio_client model."""
    return RelationshipList(**src.model_dump())
