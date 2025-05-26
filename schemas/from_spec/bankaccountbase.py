from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BankaccountBaseIn(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    bank_transactions_count: Optional[str] = None
    clio_payment_page_link: Optional[str] = None
    clio_payment_page_qr_code: Optional[str] = None
    clio_payments_enabled: Optional[str] = None
    controlled_account: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    etag: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    id: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class BankaccountBaseOut(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    bank_transactions_count: Optional[str] = None
    clio_payment_page_link: Optional[str] = None
    clio_payment_page_qr_code: Optional[str] = None
    clio_payments_enabled: Optional[str] = None
    controlled_account: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    etag: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    id: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class BankaccountBaseUpdate(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    bank_transactions_count: Optional[str] = None
    clio_payment_page_link: Optional[str] = None
    clio_payment_page_qr_code: Optional[str] = None
    clio_payments_enabled: Optional[str] = None
    controlled_account: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    etag: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    id: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class BankaccountBaseDb(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    bank_transactions_count: Optional[str] = None
    clio_payment_page_link: Optional[str] = None
    clio_payment_page_qr_code: Optional[str] = None
    clio_payments_enabled: Optional[str] = None
    controlled_account: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    etag: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    id: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

