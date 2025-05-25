from pydantic import BaseModel
from typing import Optional, List


class BillablematterIn(BaseModel):
    """Incoming model for creating a Billablematter"""
    # TODO: Add fields


class BillablematterOut(BaseModel):
    """Outgoing model for returning a Billablematter"""
    # TODO: Add fields


class BillablematterUpdate(BaseModel):
    """Update model for patching a Billablematter"""
    # TODO: Add fields


class BillablematterDb(BaseModel):
    """Internal DB representation for Billablematter"""
    # TODO: Add fields
