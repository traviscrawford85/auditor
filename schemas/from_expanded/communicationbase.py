from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    received_at: Optional[datetime] = None

class CommunicationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    received_at: Optional[datetime] = None

class CommunicationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    received_at: Optional[datetime] = None

class CommunicationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    received_at: Optional[datetime] = None

