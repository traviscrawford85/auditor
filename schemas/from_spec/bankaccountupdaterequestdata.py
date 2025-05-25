from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BankaccountupdaterequestdataIn(BaseModel):
    account_number: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None

class BankaccountupdaterequestdataOut(BaseModel):
    account_number: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None

class BankaccountupdaterequestdataUpdate(BaseModel):
    account_number: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None

class BankaccountupdaterequestdataDb(BaseModel):
    account_number: Optional[str] = None
    controlled_account: Optional[str] = None
    currency: Optional[str] = None
    default_account: Optional[str] = None
    domicile_branch: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None

