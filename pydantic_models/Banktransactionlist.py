from pydantic import BaseModel
from typing import Optional, List


class BanktransactionListIn(BaseModel):
    """Incoming model for creating a Banktransactionlist"""
    # TODO: Add fields


class BanktransactionlistOut(BaseModel):
    """Outgoing model for returning a Banktransactionlist"""
    # TODO: Add fields


class BanktransactionlistUpdate(BaseModel):
    """Update model for patching a Banktransactionlist"""
    # TODO: Add fields


class BanktransactionlistDb(BaseModel):
    """Internal DB representation for Banktransactionlist"""
    # TODO: Add fields
