from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarvisibilityIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CalendarvisibilityOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CalendarvisibilityUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CalendarvisibilityDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

