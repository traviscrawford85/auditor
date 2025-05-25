from pydantic import BaseModel
from typing import Optional, List


class BillingsettingIn(BaseModel):
    """Incoming model for creating a Billingsetting"""
    # TODO: Add fields


class BillingsettingOut(BaseModel):
    """Outgoing model for returning a Billingsetting"""
    # TODO: Add fields


class BillingsettingUpdate(BaseModel):
    """Update model for patching a Billingsetting"""
    # TODO: Add fields


class BillingsettingDb(BaseModel):
    """Internal DB representation for Billingsetting"""
    # TODO: Add fields
