from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LinkedfolderbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class LinkedfolderbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class LinkedfolderbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class LinkedfolderbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

