from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentarchiveBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[str] = None
    progress: Optional[str] = None
    state: Optional[str] = None
    message: Optional[str] = None

