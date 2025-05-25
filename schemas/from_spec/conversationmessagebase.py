from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ConversationmessagebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmessagebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmessagebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmessagebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

