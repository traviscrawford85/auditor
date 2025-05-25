from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionstotriggerBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class JurisdictionstotriggerBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class JurisdictionstotriggerBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class JurisdictionstotriggerBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

