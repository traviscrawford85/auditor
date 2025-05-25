from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ServicetypeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

class ServicetypeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

class ServicetypeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

class ServicetypeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

