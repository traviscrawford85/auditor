from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RemindertemplateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class RemindertemplateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class RemindertemplateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class RemindertemplateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    notification_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

