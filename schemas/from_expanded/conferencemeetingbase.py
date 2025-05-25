from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConferencemeetingBaseIn(BaseModel):
    conference_id: Optional[int] = None
    conference_password: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[int] = None
    updated_at: Optional[datetime] = None

class ConferencemeetingBaseOut(BaseModel):
    conference_id: Optional[int] = None
    conference_password: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[int] = None
    updated_at: Optional[datetime] = None

class ConferencemeetingBaseUpdate(BaseModel):
    conference_id: Optional[int] = None
    conference_password: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[int] = None
    updated_at: Optional[datetime] = None

class ConferencemeetingBaseDb(BaseModel):
    conference_id: Optional[int] = None
    conference_password: Optional[str] = None
    created_at: Optional[datetime] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[int] = None
    updated_at: Optional[datetime] = None

