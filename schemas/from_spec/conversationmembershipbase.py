from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmembershipbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmembershipbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    read: Optional[str] = None
    archived: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

