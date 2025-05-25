from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class OutstandingclientbalancebaseIn(BaseModel):
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

class OutstandingclientbalancebaseOut(BaseModel):
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

class OutstandingclientbalancebaseUpdate(BaseModel):
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

class OutstandingclientbalancebaseDb(BaseModel):
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

