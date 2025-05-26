from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumenttemplateBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumenttemplateBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumenttemplateBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumenttemplateBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    size: Optional[str] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

