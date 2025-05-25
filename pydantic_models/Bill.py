from pydantic import BaseModel
from typing import Optional, List


class BillIn(BaseModel):
    """Incoming model for creating a Bill"""
    # TODO: Add fields


class BillOut(BaseModel):
    """Outgoing model for returning a Bill"""
    # TODO: Add fields


class BillUpdate(BaseModel):
    """Update model for patching a Bill"""
    # TODO: Add fields


class BillDb(BaseModel):
    """Internal DB representation for Bill"""
    # TODO: Add fields
