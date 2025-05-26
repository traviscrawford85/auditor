from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktypeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TasktypeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TasktypeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TasktypeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

