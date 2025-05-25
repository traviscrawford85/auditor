from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RemindertemplatebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplatebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplatebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class RemindertemplatebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    duration: Optional[str] = None
    notification_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

