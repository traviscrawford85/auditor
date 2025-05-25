from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PaymentBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PaymentBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PaymentBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PaymentBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

