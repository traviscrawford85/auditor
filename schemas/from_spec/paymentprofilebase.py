from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PaymentprofileBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[str] = None
    name: Optional[str] = None
    terms: Optional[str] = None
    discount_rate: Optional[str] = None
    discount_period: Optional[str] = None
    interest_rate: Optional[str] = None
    interest_period: Optional[str] = None
    interest_type: Optional[str] = None

class PaymentprofileBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[str] = None
    name: Optional[str] = None
    terms: Optional[str] = None
    discount_rate: Optional[str] = None
    discount_period: Optional[str] = None
    interest_rate: Optional[str] = None
    interest_period: Optional[str] = None
    interest_type: Optional[str] = None

class PaymentprofileBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[str] = None
    name: Optional[str] = None
    terms: Optional[str] = None
    discount_rate: Optional[str] = None
    discount_period: Optional[str] = None
    interest_rate: Optional[str] = None
    interest_period: Optional[str] = None
    interest_type: Optional[str] = None

class PaymentprofileBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    billing_setting_id: Optional[str] = None
    name: Optional[str] = None
    terms: Optional[str] = None
    discount_rate: Optional[str] = None
    discount_period: Optional[str] = None
    interest_rate: Optional[str] = None
    interest_period: Optional[str] = None
    interest_type: Optional[str] = None

