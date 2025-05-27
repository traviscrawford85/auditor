from typing import Optional

from pydantic import BaseModel


class CliopaymentslinkBaseIn(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseOut(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseUpdate(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

class CliopaymentslinkBaseDb(BaseModel):
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

