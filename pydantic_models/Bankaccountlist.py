from pydantic import BaseModel
from typing import Optional, List


class BankaccountListIn(BaseModel):
    """Incoming model for creating a Bankaccountlist"""
    # TODO: Add fields


class BankaccountlistOut(BaseModel):
    """Outgoing model for returning a Bankaccountlist"""
    # TODO: Add fields


class BankaccountlistUpdate(BaseModel):
    """Update model for patching a Bankaccountlist"""
    # TODO: Add fields


class BankaccountlistDb(BaseModel):
    """Internal DB representation for Bankaccountlist"""
    # TODO: Add fields
