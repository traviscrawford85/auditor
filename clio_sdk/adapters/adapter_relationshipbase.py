# Adapter for relationshipbase
from clio_sdk.models.relationshipbase import RelationshipBaseIn, RelationshipbaseOut, RelationshipbaseUpdate, RelationshipbaseDb
from clio_client.models.relationship import Relationship

def convert_sdk_to_relationshipbaseout(src: Relationship) -> RelationshipbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return RelationshipbaseOut(**src.model_dump())

def convert_relationshipbasein_to_sdk(src: RelationshipBaseIn) -> Relationship:
    """Converts a clio_sdk model to clio_client model."""
    return Relationship(**src.model_dump())
