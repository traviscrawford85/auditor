from typing import Optional

from pydantic import BaseModel


class ExpensecategoryBaseIn(BaseModel):
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

class ExpensecategoryBaseOut(BaseModel):
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

class ExpensecategoryBaseUpdate(BaseModel):
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

class ExpensecategoryBaseDb(BaseModel):
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

