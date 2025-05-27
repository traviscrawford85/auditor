from typing import Optional

from pydantic import BaseModel


class ConversationBaseIn(BaseModel):
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

class ConversationBaseOut(BaseModel):
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

class ConversationBaseUpdate(BaseModel):
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

class ConversationBaseDb(BaseModel):
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

