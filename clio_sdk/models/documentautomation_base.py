from typing import Optional

from pydantic import BaseModel


class DocumentautomationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumentautomationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumentautomationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumentautomationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

