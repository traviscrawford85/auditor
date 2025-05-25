from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotificationeventsubscriberBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class NotificationeventsubscriberBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class NotificationeventsubscriberBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class NotificationeventsubscriberBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    user_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

