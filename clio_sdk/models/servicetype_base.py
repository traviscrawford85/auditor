from typing import Optional

from pydantic import BaseModel


class ServicetypeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

class ServicetypeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

class ServicetypeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

class ServicetypeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

