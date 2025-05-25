from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LogentrybaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentrybaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentrybaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LogentrybaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

