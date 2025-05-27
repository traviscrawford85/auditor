from typing import Optional

from pydantic import BaseModel


class JurisdictionstotriggerBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[str] = None
    is_served: Optional[str] = None
    is_requirements_required: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

