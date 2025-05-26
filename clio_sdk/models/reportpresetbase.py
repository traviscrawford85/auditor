from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportpresetBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    category: Optional[str] = None
    options: Optional[str] = None

