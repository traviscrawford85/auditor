from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PracticeareabaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareabaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareabaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

class PracticeareabaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

