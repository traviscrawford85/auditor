from typing import Optional

from pydantic import BaseModel


class BanktransactionBaseIn(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[int] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[float] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[float] = None
    funds_out: Optional[float] = None
    clio_payments_transaction: Optional[bool] = None
    current_account_balance: Optional[float] = None
    read_only_confirmation: Optional[bool] = None

class BanktransactionBaseOut(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[int] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[float] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[float] = None
    funds_out: Optional[float] = None
    clio_payments_transaction: Optional[bool] = None
    current_account_balance: Optional[float] = None
    read_only_confirmation: Optional[bool] = None

class BanktransactionBaseUpdate(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[int] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[float] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[float] = None
    funds_out: Optional[float] = None
    clio_payments_transaction: Optional[bool] = None
    current_account_balance: Optional[float] = None
    read_only_confirmation: Optional[bool] = None

class BanktransactionBaseDb(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[int] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[float] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[float] = None
    funds_out: Optional[float] = None
    clio_payments_transaction: Optional[bool] = None
    current_account_balance: Optional[float] = None
    read_only_confirmation: Optional[bool] = None

