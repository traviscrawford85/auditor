from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentspaymentBaseIn(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[datetime] = None

class CliopaymentspaymentBaseOut(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[datetime] = None

class CliopaymentspaymentBaseUpdate(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[datetime] = None

class CliopaymentspaymentBaseDb(BaseModel):
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[datetime] = None

