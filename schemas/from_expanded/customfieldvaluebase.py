from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldvalueBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    field_type: Optional[str] = None
    field_required: Optional[bool] = None
    field_displayed: Optional[bool] = None
    field_display_order: Optional[int] = None
    value: Optional[str] = None
    soft_deleted: Optional[bool] = None

class CustomfieldvalueBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    field_type: Optional[str] = None
    field_required: Optional[bool] = None
    field_displayed: Optional[bool] = None
    field_display_order: Optional[int] = None
    value: Optional[str] = None
    soft_deleted: Optional[bool] = None

class CustomfieldvalueBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    field_type: Optional[str] = None
    field_required: Optional[bool] = None
    field_displayed: Optional[bool] = None
    field_display_order: Optional[int] = None
    value: Optional[str] = None
    soft_deleted: Optional[bool] = None

class CustomfieldvalueBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    field_type: Optional[str] = None
    field_required: Optional[bool] = None
    field_displayed: Optional[bool] = None
    field_display_order: Optional[int] = None
    value: Optional[str] = None
    soft_deleted: Optional[bool] = None

