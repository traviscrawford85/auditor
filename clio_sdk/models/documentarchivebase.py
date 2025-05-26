from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentarchiveBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

class DocumentarchiveBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

