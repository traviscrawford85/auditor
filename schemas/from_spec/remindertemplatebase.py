from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RemindertemplateBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplateBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplateBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplateBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

