from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomactionBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

