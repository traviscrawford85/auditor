from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    archived: Optional[bool] = None
    read_only: Optional[bool] = None
    current_user_is_member: Optional[bool] = None
    subject: Optional[str] = None
    message_count: Optional[int] = None
    time_entries_count: Optional[int] = None
    read: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ConversationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    archived: Optional[bool] = None
    read_only: Optional[bool] = None
    current_user_is_member: Optional[bool] = None
    subject: Optional[str] = None
    message_count: Optional[int] = None
    time_entries_count: Optional[int] = None
    read: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ConversationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    archived: Optional[bool] = None
    read_only: Optional[bool] = None
    current_user_is_member: Optional[bool] = None
    subject: Optional[str] = None
    message_count: Optional[int] = None
    time_entries_count: Optional[int] = None
    read: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ConversationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    archived: Optional[bool] = None
    read_only: Optional[bool] = None
    current_user_is_member: Optional[bool] = None
    subject: Optional[str] = None
    message_count: Optional[int] = None
    time_entries_count: Optional[int] = None
    read: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

