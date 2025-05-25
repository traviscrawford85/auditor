from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EventbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    title_url: Optional[str] = None
    description: Optional[str] = None
    description_url: Optional[str] = None
    primary_detail: Optional[str] = None
    primary_detail_url: Optional[str] = None
    secondary_detail: Optional[str] = None
    secondary_detail_url: Optional[str] = None
    occurred_at: Optional[str] = None
    mobile_icon: Optional[str] = None
    subject_type: Optional[str] = None
    subject_id: Optional[str] = None

class EventbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    title_url: Optional[str] = None
    description: Optional[str] = None
    description_url: Optional[str] = None
    primary_detail: Optional[str] = None
    primary_detail_url: Optional[str] = None
    secondary_detail: Optional[str] = None
    secondary_detail_url: Optional[str] = None
    occurred_at: Optional[str] = None
    mobile_icon: Optional[str] = None
    subject_type: Optional[str] = None
    subject_id: Optional[str] = None

class EventbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    title_url: Optional[str] = None
    description: Optional[str] = None
    description_url: Optional[str] = None
    primary_detail: Optional[str] = None
    primary_detail_url: Optional[str] = None
    secondary_detail: Optional[str] = None
    secondary_detail_url: Optional[str] = None
    occurred_at: Optional[str] = None
    mobile_icon: Optional[str] = None
    subject_type: Optional[str] = None
    subject_id: Optional[str] = None

class EventbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    title_url: Optional[str] = None
    description: Optional[str] = None
    description_url: Optional[str] = None
    primary_detail: Optional[str] = None
    primary_detail_url: Optional[str] = None
    secondary_detail: Optional[str] = None
    secondary_detail_url: Optional[str] = None
    occurred_at: Optional[str] = None
    mobile_icon: Optional[str] = None
    subject_type: Optional[str] = None
    subject_id: Optional[str] = None

