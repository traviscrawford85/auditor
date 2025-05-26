from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class AllocationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    interest: Optional[bool] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    description: Optional[str] = None
    has_online_payment: Optional[bool] = None
    destroyable: Optional[bool] = None
    payment_type: Optional[str] = None

class AllocationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    interest: Optional[bool] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    description: Optional[str] = None
    has_online_payment: Optional[bool] = None
    destroyable: Optional[bool] = None
    payment_type: Optional[str] = None

class AllocationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    interest: Optional[bool] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    description: Optional[str] = None
    has_online_payment: Optional[bool] = None
    destroyable: Optional[bool] = None
    payment_type: Optional[str] = None

class AllocationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    interest: Optional[bool] = None
    voided_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    description: Optional[str] = None
    has_online_payment: Optional[bool] = None
    destroyable: Optional[bool] = None
    payment_type: Optional[str] = None

