from pydantic import BaseModel
from typing import Optional, List


class BalanceIn(BaseModel):
    """Incoming model for creating a Balance"""
    # TODO: Add fields


class BalanceOut(BaseModel):
    """Outgoing model for returning a Balance"""
    # TODO: Add fields


class BalanceUpdate(BaseModel):
    """Update model for patching a Balance"""
    # TODO: Add fields


class BalanceDb(BaseModel):
    """Internal DB representation for Balance"""
    # TODO: Add fields
