from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[str] = None
    is_local_timezone: Optional[str] = None

class JurisdictionbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[str] = None
    is_local_timezone: Optional[str] = None

class JurisdictionbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[str] = None
    is_local_timezone: Optional[str] = None

class JurisdictionbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[str] = None
    is_local_timezone: Optional[str] = None

