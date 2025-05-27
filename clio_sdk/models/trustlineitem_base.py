from typing import Optional

from pydantic import BaseModel


class TrustlineitemBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TrustlineitemBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TrustlineitemBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class TrustlineitemBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

