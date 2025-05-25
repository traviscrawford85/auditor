from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportbaseIn(BaseModel):
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

class ReportbaseOut(BaseModel):
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

class ReportbaseUpdate(BaseModel):
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

class ReportbaseDb(BaseModel):
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

