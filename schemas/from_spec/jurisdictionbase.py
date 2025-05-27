from typing import Optional

from pydantic import BaseModel


class JurisdictionBaseIn(BaseModel):
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

class JurisdictionBaseOut(BaseModel):
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

class JurisdictionBaseUpdate(BaseModel):
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

class JurisdictionBaseDb(BaseModel):
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

