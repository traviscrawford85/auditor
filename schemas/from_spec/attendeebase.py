from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AttendeebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AttendeebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AttendeebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AttendeebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

