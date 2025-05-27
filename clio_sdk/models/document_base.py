from typing import Optional

from pydantic import BaseModel


class DocumentBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

class DocumentBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

class DocumentBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

class DocumentBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

