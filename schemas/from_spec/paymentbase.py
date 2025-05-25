from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PaymentbaseIn(BaseModel):
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

class PaymentbaseOut(BaseModel):
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

class PaymentbaseUpdate(BaseModel):
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

class PaymentbaseDb(BaseModel):
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

