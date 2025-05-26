from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CommentBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CommentBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CommentBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

