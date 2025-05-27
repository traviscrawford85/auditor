from typing import Optional

from pydantic import BaseModel


class AllocationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    interest: Optional[bool] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
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
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
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
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
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
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    description: Optional[str] = None
    has_online_payment: Optional[bool] = None
    destroyable: Optional[bool] = None
    payment_type: Optional[str] = None

