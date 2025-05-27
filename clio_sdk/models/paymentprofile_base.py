from typing import Optional

from pydantic import BaseModel


class PaymentprofileBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[int] = None
    name: Optional[str] = None
    terms: Optional[int] = None
    discount_rate: Optional[float] = None
    discount_period: Optional[int] = None
    interest_rate: Optional[float] = None
    interest_period: Optional[int] = None
    interest_type: Optional[str] = None

class PaymentprofileBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[int] = None
    name: Optional[str] = None
    terms: Optional[int] = None
    discount_rate: Optional[float] = None
    discount_period: Optional[int] = None
    interest_rate: Optional[float] = None
    interest_period: Optional[int] = None
    interest_type: Optional[str] = None

class PaymentprofileBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[int] = None
    name: Optional[str] = None
    terms: Optional[int] = None
    discount_rate: Optional[float] = None
    discount_period: Optional[int] = None
    interest_rate: Optional[float] = None
    interest_period: Optional[int] = None
    interest_type: Optional[str] = None

class PaymentprofileBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[int] = None
    name: Optional[str] = None
    terms: Optional[int] = None
    discount_rate: Optional[float] = None
    discount_period: Optional[int] = None
    interest_rate: Optional[float] = None
    interest_period: Optional[int] = None
    interest_type: Optional[str] = None

