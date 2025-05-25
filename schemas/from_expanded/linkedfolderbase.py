from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LinkedfolderBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

class LinkedfolderBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

class LinkedfolderBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

class LinkedfolderBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

