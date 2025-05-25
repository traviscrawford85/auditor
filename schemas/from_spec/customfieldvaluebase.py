from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldvaluebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    field_type: Optional[str] = None
    field_required: Optional[str] = None
    field_displayed: Optional[str] = None
    field_display_order: Optional[str] = None
    value: Optional[str] = None
    soft_deleted: Optional[str] = None

class CustomfieldvaluebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    field_type: Optional[str] = None
    field_required: Optional[str] = None
    field_displayed: Optional[str] = None
    field_display_order: Optional[str] = None
    value: Optional[str] = None
    soft_deleted: Optional[str] = None

class CustomfieldvaluebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    field_type: Optional[str] = None
    field_required: Optional[str] = None
    field_displayed: Optional[str] = None
    field_display_order: Optional[str] = None
    value: Optional[str] = None
    soft_deleted: Optional[str] = None

class CustomfieldvaluebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    field_type: Optional[str] = None
    field_required: Optional[str] = None
    field_displayed: Optional[str] = None
    field_display_order: Optional[str] = None
    value: Optional[str] = None
    soft_deleted: Optional[str] = None

