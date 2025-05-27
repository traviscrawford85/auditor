from typing import Optional

from pydantic import BaseModel


class DocumenttemplateBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumenttemplateBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumenttemplateBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumenttemplateBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

