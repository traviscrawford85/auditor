from typing import Optional

from pydantic import BaseModel


class ConversationmessageBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmessageBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmessageBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class ConversationmessageBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

