from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareaBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

