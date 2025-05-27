from typing import Optional

from pydantic import BaseModel


class WebhookBaseIn(BaseModel):
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

class WebhookBaseOut(BaseModel):
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

class WebhookBaseUpdate(BaseModel):
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

class WebhookBaseDb(BaseModel):
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

