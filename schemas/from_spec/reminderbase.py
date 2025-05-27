from typing import Optional

from pydantic import BaseModel


class ReminderBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ReminderBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ReminderBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ReminderBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

