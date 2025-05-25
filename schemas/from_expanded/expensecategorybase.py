from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExpensecategoryBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[int] = None
    entry_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    tax_setting: Optional[str] = None
    currency: Optional[Any] = None

class ExpensecategoryBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[int] = None
    entry_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    tax_setting: Optional[str] = None
    currency: Optional[Any] = None

class ExpensecategoryBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[int] = None
    entry_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    tax_setting: Optional[str] = None
    currency: Optional[Any] = None

class ExpensecategoryBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[int] = None
    entry_type: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    tax_setting: Optional[str] = None
    currency: Optional[Any] = None

