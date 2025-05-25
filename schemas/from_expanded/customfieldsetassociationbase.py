from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetassociationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    display_order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CustomfieldsetassociationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    display_order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CustomfieldsetassociationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    display_order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CustomfieldsetassociationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    display_order: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

