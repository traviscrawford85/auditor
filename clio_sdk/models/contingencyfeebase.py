from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContingencyfeeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    show_contingency_award: Optional[bool] = None

class ContingencyfeeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    show_contingency_award: Optional[bool] = None

class ContingencyfeeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    show_contingency_award: Optional[bool] = None

class ContingencyfeeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    show_contingency_award: Optional[bool] = None

