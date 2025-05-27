from typing import Optional

from pydantic import BaseModel


class CustomactionBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

class CustomactionBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

