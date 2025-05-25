from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReminderbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ReminderbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ReminderbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ReminderbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

