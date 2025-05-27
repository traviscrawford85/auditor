from typing import Optional

from pydantic import BaseModel


class LogentryBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentryBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentryBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentryBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

