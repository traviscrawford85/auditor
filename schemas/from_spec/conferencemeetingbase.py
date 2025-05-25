from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConferencemeetingbaseIn(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

class ConferencemeetingbaseOut(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

class ConferencemeetingbaseUpdate(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

class ConferencemeetingbaseDb(BaseModel):
    conference_id: Optional[str] = None
    conference_password: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    join_url: Optional[str] = None
    type: Optional[str] = None
    source_id: Optional[str] = None
    updated_at: Optional[str] = None

