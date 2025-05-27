from typing import List, Optional

from pydantic import BaseModel


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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

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
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

