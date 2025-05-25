from pydantic import BaseModel
from typing import Optional, List


class BillablemattershowIn(BaseModel):
    """Incoming model for creating a Billablemattershow"""
    # TODO: Add fields


class BillablemattershowOut(BaseModel):
    """Outgoing model for returning a Billablemattershow"""
    # TODO: Add fields


class BillablemattershowUpdate(BaseModel):
    """Update model for patching a Billablemattershow"""
    # TODO: Add fields


class BillablemattershowDb(BaseModel):
    """Internal DB representation for Billablemattershow"""
    # TODO: Add fields
