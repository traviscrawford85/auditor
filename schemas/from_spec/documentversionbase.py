from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DocumentversionbaseIn(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    version_number: Optional[str] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[str] = None

class DocumentversionbaseOut(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    version_number: Optional[str] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[str] = None

class DocumentversionbaseUpdate(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    version_number: Optional[str] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[str] = None

class DocumentversionbaseDb(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[str] = None
    version_number: Optional[str] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[str] = None

