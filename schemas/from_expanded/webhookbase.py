from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebhookBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class WebhookBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class WebhookBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class WebhookBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

