from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivityratebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

class ActivityratebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

class ActivityratebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

class ActivityratebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    rate: Optional[str] = None
    flat_rate: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[str] = None
    co_counsel_contact_id: Optional[str] = None

