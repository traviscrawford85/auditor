from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AttendeeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AttendeeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AttendeeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AttendeeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

