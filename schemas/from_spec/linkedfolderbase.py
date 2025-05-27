from typing import Optional

from pydantic import BaseModel


class LinkedfolderBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class LinkedfolderBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class LinkedfolderBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class LinkedfolderBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

