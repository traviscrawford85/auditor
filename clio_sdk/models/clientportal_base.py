from typing import Optional

from pydantic import BaseModel


class ClientportalBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

class ClientportalBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

class ClientportalBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

class ClientportalBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None

