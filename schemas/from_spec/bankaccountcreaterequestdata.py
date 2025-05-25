from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BankaccountcreaterequestdataIn(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: str
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: str

class BankaccountcreaterequestdataOut(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: str
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: str

class BankaccountcreaterequestdataUpdate(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: str
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: str

class BankaccountcreaterequestdataDb(BaseModel):
    account_number: Optional[str] = None
    balance: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: str
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: str

