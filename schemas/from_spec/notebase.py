from typing import Optional

from pydantic import BaseModel


class NoteBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

class NoteBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

class NoteBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

class NoteBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[str] = None

