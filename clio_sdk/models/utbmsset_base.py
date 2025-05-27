from typing import Optional

from pydantic import BaseModel


class UtbmssetBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UtbmssetBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

