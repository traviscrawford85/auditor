from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ItembaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None

class ItembaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None

class ItembaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None

class ItembaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None

