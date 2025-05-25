from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommunicationbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

class CommunicationbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

class CommunicationbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

class CommunicationbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

