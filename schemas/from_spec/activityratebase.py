from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityrateBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

class ActivityrateBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

class ActivityrateBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

class ActivityrateBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

