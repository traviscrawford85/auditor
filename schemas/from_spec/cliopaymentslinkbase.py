from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentslinkBaseIn(BaseModel):
    active: Optional[str] = None
    amount: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[str] = None
    is_allocated_as_revenue: Optional[str] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseOut(BaseModel):
    active: Optional[str] = None
    amount: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[str] = None
    is_allocated_as_revenue: Optional[str] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseUpdate(BaseModel):
    active: Optional[str] = None
    amount: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[str] = None
    is_allocated_as_revenue: Optional[str] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseDb(BaseModel):
    active: Optional[str] = None
    amount: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[str] = None
    is_allocated_as_revenue: Optional[str] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

