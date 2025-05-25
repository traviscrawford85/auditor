from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelationshipListIn(BaseModel):
    data: List[Any]

class RelationshipListOut(BaseModel):
    data: List[Any]

class RelationshipListUpdate(BaseModel):
    data: List[Any]

class RelationshipListDb(BaseModel):
    data: List[Any]

