from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class InterestchargeBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class InterestchargeBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class InterestchargeBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class InterestchargeBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

