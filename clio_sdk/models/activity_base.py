from typing import Optional

from pydantic import BaseModel


class ActivityBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[float] = None
    rounded_quantity_in_hours: Optional[float] = None
    quantity: Optional[float] = None
    rounded_quantity: Optional[float] = None
    quantity_redacted: Optional[bool] = None
    price: Optional[float] = None
    note: Optional[str] = None
    flat_rate: Optional[bool] = None
    billed: Optional[bool] = None
    on_bill: Optional[bool] = None
    total: Optional[float] = None
    contingency_fee: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[bool] = None
    non_billable_total: Optional[float] = None
    no_charge: Optional[bool] = None
    tax_setting: Optional[str] = None

class ActivityBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[float] = None
    rounded_quantity_in_hours: Optional[float] = None
    quantity: Optional[float] = None
    rounded_quantity: Optional[float] = None
    quantity_redacted: Optional[bool] = None
    price: Optional[float] = None
    note: Optional[str] = None
    flat_rate: Optional[bool] = None
    billed: Optional[bool] = None
    on_bill: Optional[bool] = None
    total: Optional[float] = None
    contingency_fee: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[bool] = None
    non_billable_total: Optional[float] = None
    no_charge: Optional[bool] = None
    tax_setting: Optional[str] = None

class ActivityBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[float] = None
    rounded_quantity_in_hours: Optional[float] = None
    quantity: Optional[float] = None
    rounded_quantity: Optional[float] = None
    quantity_redacted: Optional[bool] = None
    price: Optional[float] = None
    note: Optional[str] = None
    flat_rate: Optional[bool] = None
    billed: Optional[bool] = None
    on_bill: Optional[bool] = None
    total: Optional[float] = None
    contingency_fee: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[bool] = None
    non_billable_total: Optional[float] = None
    no_charge: Optional[bool] = None
    tax_setting: Optional[str] = None

class ActivityBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[float] = None
    rounded_quantity_in_hours: Optional[float] = None
    quantity: Optional[float] = None
    rounded_quantity: Optional[float] = None
    quantity_redacted: Optional[bool] = None
    price: Optional[float] = None
    note: Optional[str] = None
    flat_rate: Optional[bool] = None
    billed: Optional[bool] = None
    on_bill: Optional[bool] = None
    total: Optional[float] = None
    contingency_fee: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[bool] = None
    non_billable_total: Optional[float] = None
    no_charge: Optional[bool] = None
    tax_setting: Optional[str] = None

