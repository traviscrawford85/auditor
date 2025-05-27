from typing import Optional

from pydantic import BaseModel


class CustomactionIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

