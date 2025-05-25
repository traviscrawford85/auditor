from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class InterestchargebaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class InterestchargebaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class InterestchargebaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class InterestchargebaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

