from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[bool] = None
    is_local_timezone: Optional[bool] = None

class JurisdictionBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[bool] = None
    is_local_timezone: Optional[bool] = None

class JurisdictionBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[bool] = None
    is_local_timezone: Optional[bool] = None

class JurisdictionBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[bool] = None
    is_local_timezone: Optional[bool] = None

