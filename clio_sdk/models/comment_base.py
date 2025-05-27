from typing import Optional

from pydantic import BaseModel


class CommentBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CommentBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

