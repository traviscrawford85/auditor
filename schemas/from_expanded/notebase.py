from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class NoteBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    detail_text_type: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    time_entries_count: Optional[int] = None

class NoteBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    detail_text_type: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    time_entries_count: Optional[int] = None

class NoteBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    detail_text_type: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    time_entries_count: Optional[int] = None

class NoteBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    detail_text_type: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    time_entries_count: Optional[int] = None

