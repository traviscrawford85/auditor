from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentautomationbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumentautomationbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumentautomationbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumentautomationbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

