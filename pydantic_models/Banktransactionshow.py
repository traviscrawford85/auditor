from pydantic import BaseModel
from typing import Optional, List


class BanktransactionShowIn(BaseModel):
    """Incoming model for creating a Banktransactionshow"""
    # TODO: Add fields


class BanktransactionshowOut(BaseModel):
    """Outgoing model for returning a Banktransactionshow"""
    # TODO: Add fields


class BanktransactionShowUpdate(BaseModel):
    """Update model for patching a Banktransactionshow"""
    # TODO: Add fields


class BanktransactionshowDb(BaseModel):
    """Internal DB representation for Banktransactionshow"""
    # TODO: Add fields
