from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionstotriggerbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

