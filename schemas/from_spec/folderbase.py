from typing import Optional

from pydantic import BaseModel


class FolderBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class FolderBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class FolderBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

class FolderBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[str] = None
    name: Optional[str] = None
    root: Optional[str] = None

