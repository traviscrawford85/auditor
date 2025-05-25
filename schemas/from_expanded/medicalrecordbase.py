from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordBaseIn(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MedicalrecordBaseOut(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MedicalrecordBaseUpdate(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MedicalrecordBaseDb(BaseModel):
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

