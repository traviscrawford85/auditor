from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentautomationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DocumentautomationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DocumentautomationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DocumentautomationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

