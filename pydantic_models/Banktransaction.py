from pydantic import BaseModel
from typing import Optional, List


class BanktransactionIn(BaseModel):
    """Incoming model for creating a Banktransaction"""
    # TODO: Add fields


class BanktransactionOut(BaseModel):
    """Outgoing model for returning a Banktransaction"""
    # TODO: Add fields


class BanktransactionUpdate(BaseModel):
    """Update model for patching a Banktransaction"""
    # TODO: Add fields


class BanktransactionDb(BaseModel):
    """Internal DB representation for Banktransaction"""
    # TODO: Add fields
