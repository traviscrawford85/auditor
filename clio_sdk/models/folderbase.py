from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class FolderBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

class FolderBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

class FolderBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

class FolderBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

