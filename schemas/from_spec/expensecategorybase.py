from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExpensecategorybaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    entry_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

class ExpensecategorybaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    entry_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

class ExpensecategorybaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    entry_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

class ExpensecategorybaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[str] = None
    entry_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    tax_setting: Optional[str] = None
    currency: Optional[str] = None

