from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NotificationeventsubscriberbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class NotificationeventsubscriberbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    user_id: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

