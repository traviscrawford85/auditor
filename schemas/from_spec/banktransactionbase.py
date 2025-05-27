from typing import Optional

from pydantic import BaseModel


class BanktransactionBaseIn(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[str] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[str] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[str] = None
    funds_out: Optional[str] = None
    clio_payments_transaction: Optional[str] = None
    current_account_balance: Optional[str] = None
    read_only_confirmation: Optional[str] = None

class BanktransactionBaseOut(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[str] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[str] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[str] = None
    funds_out: Optional[str] = None
    clio_payments_transaction: Optional[str] = None
    current_account_balance: Optional[str] = None
    read_only_confirmation: Optional[str] = None

class BanktransactionBaseUpdate(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[str] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[str] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[str] = None
    funds_out: Optional[str] = None
    clio_payments_transaction: Optional[str] = None
    current_account_balance: Optional[str] = None
    read_only_confirmation: Optional[str] = None

class BanktransactionBaseDb(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[str] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[str] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[str] = None
    funds_out: Optional[str] = None
    clio_payments_transaction: Optional[str] = None
    current_account_balance: Optional[str] = None
    read_only_confirmation: Optional[str] = None

