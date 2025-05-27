from typing import Optional

from pydantic import BaseModel


class CommunicationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

class CommunicationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

class CommunicationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

class CommunicationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

