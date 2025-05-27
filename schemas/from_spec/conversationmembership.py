from typing import Optional

from pydantic import BaseModel


class ConversationmembershipIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    member: Optional[str] = None

class ConversationmembershipOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    member: Optional[str] = None

class ConversationmembershipUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    member: Optional[str] = None

class ConversationmembershipDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    member: Optional[str] = None

