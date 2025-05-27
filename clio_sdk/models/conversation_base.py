from typing import Optional

from pydantic import BaseModel


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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

