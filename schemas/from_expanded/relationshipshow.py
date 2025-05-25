from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelationshipShowIn(BaseModel):
    data: Any

class RelationshipShowOut(BaseModel):
    data: Any

class RelationshipShowUpdate(BaseModel):
    data: Any

class RelationshipShowDb(BaseModel):
    data: Any

