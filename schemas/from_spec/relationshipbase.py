from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelationshipbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RelationshipbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

