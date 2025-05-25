from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContingencyfeebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

class ContingencyfeebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

class ContingencyfeebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

class ContingencyfeebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    show_contingency_award: Optional[str] = None

