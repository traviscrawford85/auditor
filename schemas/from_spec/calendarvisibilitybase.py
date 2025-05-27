from typing import Optional

from pydantic import BaseModel


class CalendarvisibilityBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CalendarvisibilityBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CalendarvisibilityBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CalendarvisibilityBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

