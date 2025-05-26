from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotificationmethodBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class NotificationmethodBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class NotificationmethodBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class NotificationmethodBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

