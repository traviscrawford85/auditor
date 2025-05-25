from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PicklistoptionbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

class PicklistoptionbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

class PicklistoptionbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

class PicklistoptionbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

