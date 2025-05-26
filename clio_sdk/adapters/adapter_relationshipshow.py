# Adapter for relationshipshow
from clio_sdk.models.relationshipshow import RelationshipshowIn, RelationshipshowOut, RelationshipshowUpdate, RelationshipshowDb
from clio_client.models.relationship_show import RelationshipShow

def convert_sdk_to_relationshipshowout(src: RelationshipShow) -> RelationshipshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return RelationshipshowOut(**src.model_dump())

def convert_relationshipshowin_to_sdk(src: RelationshipshowIn) -> RelationshipShow:
    """Converts a clio_sdk model to clio_client model."""
    return RelationshipShow(**src.model_dump())
