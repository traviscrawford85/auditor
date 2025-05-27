from typing import Optional

from pydantic import BaseModel


class CustomfieldBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[bool] = None
    deleted: Optional[bool] = None
    required: Optional[bool] = None
    display_order: Optional[int] = None

class CustomfieldBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[bool] = None
    deleted: Optional[bool] = None
    required: Optional[bool] = None
    display_order: Optional[int] = None

class CustomfieldBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[bool] = None
    deleted: Optional[bool] = None
    required: Optional[bool] = None
    display_order: Optional[int] = None

class CustomfieldBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[bool] = None
    deleted: Optional[bool] = None
    required: Optional[bool] = None
    display_order: Optional[int] = None

