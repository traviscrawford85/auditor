from typing import Optional

from pydantic import BaseModel


class ConversationmembershipBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

