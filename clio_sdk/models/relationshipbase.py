from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelationshipBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class RelationshipBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class RelationshipBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class RelationshipBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

