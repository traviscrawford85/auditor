from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelationshipShowIn(BaseModel):
    data: Relationship

class RelationshipShowOut(BaseModel):
    data: Relationship

class RelationshipShowUpdate(BaseModel):
    data: Relationship

class RelationshipShowDb(BaseModel):
    data: Relationship

