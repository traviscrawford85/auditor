from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentslinkBaseIn(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[datetime] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseOut(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[datetime] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseUpdate(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[datetime] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseDb(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[datetime] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[datetime] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

