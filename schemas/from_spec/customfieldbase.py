from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[str] = None
    deleted: Optional[str] = None
    required: Optional[str] = None
    display_order: Optional[str] = None

class CustomfieldbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[str] = None
    deleted: Optional[str] = None
    required: Optional[str] = None
    display_order: Optional[str] = None

class CustomfieldbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[str] = None
    deleted: Optional[str] = None
    required: Optional[str] = None
    display_order: Optional[str] = None

class CustomfieldbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[str] = None
    deleted: Optional[str] = None
    required: Optional[str] = None
    display_order: Optional[str] = None

