from typing import Optional

from pydantic import BaseModel


class AllocationBaseIn(BaseModel):
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

class AllocationBaseOut(BaseModel):
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

class AllocationBaseUpdate(BaseModel):
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

class AllocationBaseDb(BaseModel):
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

