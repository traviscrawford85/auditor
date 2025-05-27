from typing import Optional

from pydantic import BaseModel


class MedicalrecordBaseIn(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordBaseOut(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordBaseUpdate(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordBaseDb(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

