from typing import Optional

from pydantic import BaseModel


class EventBaseIn(BaseModel):
    id: Optional[int] = None
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
    subject_id: Optional[int] = None

class EventBaseOut(BaseModel):
    id: Optional[int] = None
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
    subject_id: Optional[int] = None

class EventBaseUpdate(BaseModel):
    id: Optional[int] = None
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
    subject_id: Optional[int] = None

class EventBaseDb(BaseModel):
    id: Optional[int] = None
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
    subject_id: Optional[int] = None

