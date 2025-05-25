from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ClientportalbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

class ClientportalbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

class ClientportalbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

class ClientportalbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

