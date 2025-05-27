from typing import Optional

from pydantic import BaseModel


class CustomfieldsetBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CustomfieldsetBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

