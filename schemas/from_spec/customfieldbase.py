from typing import Optional

from pydantic import BaseModel


class CustomfieldBaseIn(BaseModel):
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

class CustomfieldBaseOut(BaseModel):
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

class CustomfieldBaseUpdate(BaseModel):
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

class CustomfieldBaseDb(BaseModel):
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

