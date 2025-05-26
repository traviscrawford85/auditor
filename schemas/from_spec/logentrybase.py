from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LogentryBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentryBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentryBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentryBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

