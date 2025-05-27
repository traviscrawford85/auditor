from typing import Optional

from pydantic import BaseModel


class ServicetypeBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

class ServicetypeBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

class ServicetypeBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

class ServicetypeBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[str] = None
    description: Optional[str] = None
    default: Optional[str] = None

