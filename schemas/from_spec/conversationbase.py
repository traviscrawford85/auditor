from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    archived: Optional[str] = None
    read_only: Optional[str] = None
    current_user_is_member: Optional[str] = None
    subject: Optional[str] = None
    message_count: Optional[str] = None
    time_entries_count: Optional[str] = None
    read: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    archived: Optional[str] = None
    read_only: Optional[str] = None
    current_user_is_member: Optional[str] = None
    subject: Optional[str] = None
    message_count: Optional[str] = None
    time_entries_count: Optional[str] = None
    read: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    archived: Optional[str] = None
    read_only: Optional[str] = None
    current_user_is_member: Optional[str] = None
    subject: Optional[str] = None
    message_count: Optional[str] = None
    time_entries_count: Optional[str] = None
    read: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    archived: Optional[str] = None
    read_only: Optional[str] = None
    current_user_is_member: Optional[str] = None
    subject: Optional[str] = None
    message_count: Optional[str] = None
    time_entries_count: Optional[str] = None
    read: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

