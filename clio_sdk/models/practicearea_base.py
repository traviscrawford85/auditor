from typing import Optional

from pydantic import BaseModel


class PracticeareaBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

