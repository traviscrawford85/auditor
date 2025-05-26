from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class OutstandingclientbalanceBaseIn(BaseModel):
    associated_matter_ids: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[str] = None
    reminders_enabled: Optional[str] = None
    total_outstanding_balance: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class OutstandingclientbalanceBaseOut(BaseModel):
    associated_matter_ids: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[str] = None
    reminders_enabled: Optional[str] = None
    total_outstanding_balance: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class OutstandingclientbalanceBaseUpdate(BaseModel):
    associated_matter_ids: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[str] = None
    reminders_enabled: Optional[str] = None
    total_outstanding_balance: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class OutstandingclientbalanceBaseDb(BaseModel):
    associated_matter_ids: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[str] = None
    reminders_enabled: Optional[str] = None
    total_outstanding_balance: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

