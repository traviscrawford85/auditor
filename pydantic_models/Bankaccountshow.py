from pydantic import BaseModel
from typing import Optional, List


class BankaccountShowIn(BaseModel):
    """Incoming model for creating a Bankaccountshow"""
    # TODO: Add fields


class BankaccountshowOut(BaseModel):
    """Outgoing model for returning a Bankaccountshow"""
    # TODO: Add fields


class BankaccountShowUpdate(BaseModel):
    """Update model for patching a Bankaccountshow"""
    # TODO: Add fields


class BankaccountshowDb(BaseModel):
    """Internal DB representation for Bankaccountshow"""
    # TODO: Add fields
