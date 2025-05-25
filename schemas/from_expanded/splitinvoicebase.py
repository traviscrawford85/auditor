from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class SplitinvoiceBaseIn(BaseModel):
    id: Optional[int] = None
    bill_id: Optional[int] = None
    linked_invoices_display_numbers: Optional[List[str]] = None
    linked_invoices_ids: Optional[List[int]] = None
    split_connection_id: Optional[str] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SplitinvoiceBaseOut(BaseModel):
    id: Optional[int] = None
    bill_id: Optional[int] = None
    linked_invoices_display_numbers: Optional[List[str]] = None
    linked_invoices_ids: Optional[List[int]] = None
    split_connection_id: Optional[str] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SplitinvoiceBaseUpdate(BaseModel):
    id: Optional[int] = None
    bill_id: Optional[int] = None
    linked_invoices_display_numbers: Optional[List[str]] = None
    linked_invoices_ids: Optional[List[int]] = None
    split_connection_id: Optional[str] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SplitinvoiceBaseDb(BaseModel):
    id: Optional[int] = None
    bill_id: Optional[int] = None
    linked_invoices_display_numbers: Optional[List[str]] = None
    linked_invoices_ids: Optional[List[int]] = None
    split_connection_id: Optional[str] = None
    split_portion: Optional[float] = None
    etag: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

