from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    source: Optional[str] = None

class ReportBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    source: Optional[str] = None

