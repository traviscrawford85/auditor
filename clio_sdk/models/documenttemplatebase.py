from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumenttemplateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DocumenttemplateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DocumenttemplateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DocumenttemplateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

