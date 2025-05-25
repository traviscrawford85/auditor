from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

class DocumentBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

class DocumentBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

class DocumentBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

