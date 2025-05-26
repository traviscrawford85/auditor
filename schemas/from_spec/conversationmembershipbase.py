from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmembershipBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

