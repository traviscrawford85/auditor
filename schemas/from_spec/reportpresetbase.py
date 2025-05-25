from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportpresetbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

class ReportpresetbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

