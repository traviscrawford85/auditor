from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CreditmemobaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemobaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemobaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class CreditmemobaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    description: Optional[str] = None
    discount: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

