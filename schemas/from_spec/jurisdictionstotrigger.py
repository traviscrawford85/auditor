from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionstotriggerIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

