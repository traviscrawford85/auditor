from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotificationeventsubscriberBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

