from typing import Optional

from pydantic import BaseModel


class NotificationmethodBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationmethodBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    email_address: Optional[str] = None
    is_default_email_address: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

