from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CommentbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

