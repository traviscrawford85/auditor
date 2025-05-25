from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AllocationbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    interest: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    description: Optional[str] = None
    has_online_payment: Optional[str] = None
    destroyable: Optional[str] = None
    payment_type: Optional[str] = None

class AllocationbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    interest: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    description: Optional[str] = None
    has_online_payment: Optional[str] = None
    destroyable: Optional[str] = None
    payment_type: Optional[str] = None

class AllocationbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    interest: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    description: Optional[str] = None
    has_online_payment: Optional[str] = None
    destroyable: Optional[str] = None
    payment_type: Optional[str] = None

class AllocationbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    interest: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    description: Optional[str] = None
    has_online_payment: Optional[str] = None
    destroyable: Optional[str] = None
    payment_type: Optional[str] = None

