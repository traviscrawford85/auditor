from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustlineitemBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TrustlineitemBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TrustlineitemBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TrustlineitemBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

