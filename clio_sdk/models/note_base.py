from typing import Optional

from pydantic import BaseModel


class NoteBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

class NoteBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

class NoteBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

class NoteBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

