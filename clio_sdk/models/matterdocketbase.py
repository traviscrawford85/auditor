from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterdocketBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    start_date: Optional[str] = None
    start_time: Optional[datetime] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

class MatterdocketBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    start_date: Optional[str] = None
    start_time: Optional[datetime] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

class MatterdocketBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    start_date: Optional[str] = None
    start_time: Optional[datetime] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

class MatterdocketBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    start_date: Optional[str] = None
    start_time: Optional[datetime] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

