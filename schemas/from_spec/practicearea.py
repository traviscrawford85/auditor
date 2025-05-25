from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareaIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareaDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

