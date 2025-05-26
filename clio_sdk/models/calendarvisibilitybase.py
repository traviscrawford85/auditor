from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CalendarvisibilityBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[bool] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CalendarvisibilityBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[bool] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CalendarvisibilityBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[bool] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CalendarvisibilityBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[bool] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

