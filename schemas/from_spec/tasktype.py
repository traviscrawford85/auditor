from typing import Optional

from pydantic import BaseModel


class TasktypeIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktypeOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktypeUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TasktypeDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

