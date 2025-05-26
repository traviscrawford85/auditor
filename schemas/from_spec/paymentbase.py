from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PaymentBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PaymentBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PaymentBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class PaymentBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[str] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

