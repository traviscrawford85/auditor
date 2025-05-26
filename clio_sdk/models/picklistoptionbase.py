from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PicklistoptionBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    option: Optional[str] = None
    deleted_at: Optional[datetime] = None

class PicklistoptionBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    option: Optional[str] = None
    deleted_at: Optional[datetime] = None

class PicklistoptionBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    option: Optional[str] = None
    deleted_at: Optional[datetime] = None

class PicklistoptionBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    option: Optional[str] = None
    deleted_at: Optional[datetime] = None

