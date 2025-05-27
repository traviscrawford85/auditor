from typing import Optional

from pydantic import BaseModel


class ClientportalBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

class ClientportalBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

class ClientportalBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

class ClientportalBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[str] = None
    unread_notifiable_count: Optional[str] = None

