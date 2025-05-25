from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitybaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[str] = None
    rounded_quantity_in_hours: Optional[str] = None
    quantity: Optional[str] = None
    rounded_quantity: Optional[str] = None
    quantity_redacted: Optional[str] = None
    price: Optional[str] = None
    note: Optional[str] = None
    flat_rate: Optional[str] = None
    billed: Optional[str] = None
    on_bill: Optional[str] = None
    total: Optional[str] = None
    contingency_fee: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[str] = None
    non_billable_total: Optional[str] = None
    no_charge: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

class ActivitybaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[str] = None
    rounded_quantity_in_hours: Optional[str] = None
    quantity: Optional[str] = None
    rounded_quantity: Optional[str] = None
    quantity_redacted: Optional[str] = None
    price: Optional[str] = None
    note: Optional[str] = None
    flat_rate: Optional[str] = None
    billed: Optional[str] = None
    on_bill: Optional[str] = None
    total: Optional[str] = None
    contingency_fee: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[str] = None
    non_billable_total: Optional[str] = None
    no_charge: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

class ActivitybaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[str] = None
    rounded_quantity_in_hours: Optional[str] = None
    quantity: Optional[str] = None
    rounded_quantity: Optional[str] = None
    quantity_redacted: Optional[str] = None
    price: Optional[str] = None
    note: Optional[str] = None
    flat_rate: Optional[str] = None
    billed: Optional[str] = None
    on_bill: Optional[str] = None
    total: Optional[str] = None
    contingency_fee: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[str] = None
    non_billable_total: Optional[str] = None
    no_charge: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

class ActivitybaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[str] = None
    rounded_quantity_in_hours: Optional[str] = None
    quantity: Optional[str] = None
    rounded_quantity: Optional[str] = None
    quantity_redacted: Optional[str] = None
    price: Optional[str] = None
    note: Optional[str] = None
    flat_rate: Optional[str] = None
    billed: Optional[str] = None
    on_bill: Optional[str] = None
    total: Optional[str] = None
    contingency_fee: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[str] = None
    non_billable_total: Optional[str] = None
    no_charge: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

