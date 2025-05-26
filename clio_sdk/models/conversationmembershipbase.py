from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmembershipBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ConversationmembershipBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ConversationmembershipBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ConversationmembershipBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

