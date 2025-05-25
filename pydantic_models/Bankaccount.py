from pydantic import BaseModel
from typing import Optional, List


class BankaccountIn(BaseModel):
    """Incoming model for creating a Bankaccount"""
    # TODO: Add fields


class BankaccountOut(BaseModel):
    """Outgoing model for returning a Bankaccount"""
    # TODO: Add fields


class BankaccountUpdate(BaseModel):
    """Update model for patching a Bankaccount"""
    # TODO: Add fields


class BankaccountDb(BaseModel):
    """Internal DB representation for Bankaccount"""
    # TODO: Add fields
