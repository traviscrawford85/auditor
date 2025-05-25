from pydantic import BaseModel
from typing import Optional, List


class BillshowIn(BaseModel):
    """Incoming model for creating a Billshow"""
    # TODO: Add fields


class BillshowOut(BaseModel):
    """Outgoing model for returning a Billshow"""
    # TODO: Add fields


class BillshowUpdate(BaseModel):
    """Update model for patching a Billshow"""
    # TODO: Add fields


class BillshowDb(BaseModel):
    """Internal DB representation for Billshow"""
    # TODO: Add fields
