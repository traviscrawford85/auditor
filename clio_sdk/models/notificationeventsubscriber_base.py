from typing import Optional

from pydantic import BaseModel


class NotificationeventsubscriberBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

