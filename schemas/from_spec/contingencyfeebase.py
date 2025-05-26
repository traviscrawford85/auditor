from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContingencyfeeBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

class ContingencyfeeBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

class ContingencyfeeBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

class ContingencyfeeBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

