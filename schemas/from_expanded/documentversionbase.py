from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentversionBaseIn(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[datetime] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

class DocumentversionBaseOut(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[datetime] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

class DocumentversionBaseUpdate(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[datetime] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

class DocumentversionBaseDb(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[datetime] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

