from typing import Optional

from pydantic import BaseModel


class DocumentversionBaseIn(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

class DocumentversionBaseOut(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

class DocumentversionBaseUpdate(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

class DocumentversionBaseDb(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

