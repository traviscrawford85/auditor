from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelationshipListIn(BaseModel):
    data: List[Relationship]

class RelationshipListOut(BaseModel):
    data: List[Relationship]

class RelationshipListUpdate(BaseModel):
    data: List[Relationship]

class RelationshipListDb(BaseModel):
    data: List[Relationship]

