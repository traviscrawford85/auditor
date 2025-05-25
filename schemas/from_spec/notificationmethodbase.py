from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotificationmethodbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

