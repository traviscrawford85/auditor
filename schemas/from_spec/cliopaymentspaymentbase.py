from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentspaymentbaseIn(BaseModel):
    amount: Optional[str] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[str] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

class CliopaymentspaymentbaseOut(BaseModel):
    amount: Optional[str] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[str] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

class CliopaymentspaymentbaseUpdate(BaseModel):
    amount: Optional[str] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[str] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

class CliopaymentspaymentbaseDb(BaseModel):
    amount: Optional[str] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[str] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

