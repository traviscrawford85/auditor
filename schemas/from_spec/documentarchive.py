from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentarchiveIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

