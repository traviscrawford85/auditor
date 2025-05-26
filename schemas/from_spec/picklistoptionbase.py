from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PicklistoptionBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

class PicklistoptionBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

class PicklistoptionBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

class PicklistoptionBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

