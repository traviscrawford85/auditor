from typing import Optional

from pydantic import BaseModel


class JurisdictionstotriggerBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class JurisdictionstotriggerBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

