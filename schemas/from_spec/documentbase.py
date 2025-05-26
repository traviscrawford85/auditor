from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None

class DocumentBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None

class DocumentBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None

class DocumentBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None

