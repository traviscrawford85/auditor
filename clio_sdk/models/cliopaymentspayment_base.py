from typing import Optional

from pydantic import BaseModel


class CliopaymentspaymentBaseIn(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

class CliopaymentspaymentBaseOut(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

class CliopaymentspaymentBaseUpdate(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

class CliopaymentspaymentBaseDb(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

