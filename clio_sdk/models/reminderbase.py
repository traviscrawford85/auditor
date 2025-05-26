from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReminderBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    next_delivery_at: Optional[datetime] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ReminderBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    next_delivery_at: Optional[datetime] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ReminderBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    next_delivery_at: Optional[datetime] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ReminderBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    next_delivery_at: Optional[datetime] = None
    state: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

