from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

