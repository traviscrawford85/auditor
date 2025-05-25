from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class OutstandingclientbalanceBaseIn(BaseModel):
    associated_matter_ids: Optional[List[int]] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[float] = None
    reminders_enabled: Optional[bool] = None
    total_outstanding_balance: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class OutstandingclientbalanceBaseOut(BaseModel):
    associated_matter_ids: Optional[List[int]] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[float] = None
    reminders_enabled: Optional[bool] = None
    total_outstanding_balance: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class OutstandingclientbalanceBaseUpdate(BaseModel):
    associated_matter_ids: Optional[List[int]] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[float] = None
    reminders_enabled: Optional[bool] = None
    total_outstanding_balance: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class OutstandingclientbalanceBaseDb(BaseModel):
    associated_matter_ids: Optional[List[int]] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[float] = None
    reminders_enabled: Optional[bool] = None
    total_outstanding_balance: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

