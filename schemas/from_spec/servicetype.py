from typing import Optional

from pydantic import BaseModel


class ServicetypeIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

class ServicetypeOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

class ServicetypeUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

class ServicetypeDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

