from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ClientportalBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

class ClientportalBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

class ClientportalBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

class ClientportalBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

