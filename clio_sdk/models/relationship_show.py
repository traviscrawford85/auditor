
from pydantic import BaseModel

from .relationship import RelationshipOut


class RelationshipShowIn(BaseModel):
    data: RelationshipIn

class RelationshipShowOut(BaseModel):
    data: RelationshipOut

class RelationshipShowUpdate(BaseModel):
    data: RelationshipUpdate

class RelationshipShowDb(BaseModel):
    data: RelationshipDb

