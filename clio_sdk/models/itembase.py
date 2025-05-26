from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ItemBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None

class ItemBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None

class ItemBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None

class ItemBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None

