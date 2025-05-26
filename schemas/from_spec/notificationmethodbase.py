from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotificationmethodBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

