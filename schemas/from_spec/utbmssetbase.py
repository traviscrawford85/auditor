from typing import Optional

from pydantic import BaseModel


class UtbmssetBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

