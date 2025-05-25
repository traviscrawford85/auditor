from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebhookbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[str] = None
    expires_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebhookbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[str] = None
    expires_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebhookbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[str] = None
    expires_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class WebhookbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[str] = None
    expires_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

