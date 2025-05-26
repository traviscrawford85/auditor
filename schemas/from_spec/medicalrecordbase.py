from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordBaseIn(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordBaseOut(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordBaseUpdate(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordBaseDb(BaseModel):
    id: Optional[str] = None
    document_id: Optional[str] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

