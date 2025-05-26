# Adapter for relationshipshow
from clio_sdk.models.relationshipshow import RelationshipshowIn, RelationshipshowOut, RelationshipshowUpdate, RelationshipshowDb
from clio_client.models import relationship_show

def convert_sdk_to_relationshipshowout(src: relationship_show) -> RelationshipshowOut:
    return RelationshipshowOut(**src.dict())

def convert_relationshipshowin_to_sdk(src: RelationshipshowIn) -> relationship_show:
    return relationship_show(**src.dict())
