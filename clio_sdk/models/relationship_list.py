from typing import List

from pydantic import BaseModel

from .relationship import RelationshipOut


class RelationshipListIn(BaseModel):
    data: List[RelationshipIn]

class RelationshipListOut(BaseModel):
    data: List[RelationshipOut]

class RelationshipListUpdate(BaseModel):
    data: List[RelationshipUpdate]

class RelationshipListDb(BaseModel):
    data: List[RelationshipDb]

