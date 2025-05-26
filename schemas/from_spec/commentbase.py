from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

