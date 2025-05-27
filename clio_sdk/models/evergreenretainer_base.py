from typing import Optional

from pydantic import BaseModel


class EvergreenretainerBaseIn(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

class EvergreenretainerBaseOut(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

class EvergreenretainerBaseUpdate(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

class EvergreenretainerBaseDb(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    etag: Optional[str] = None
    minimum_threshold: Optional[float] = None

