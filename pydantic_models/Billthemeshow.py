from pydantic import BaseModel
from typing import Optional, List


class BillthemeShowIn(BaseModel):
    """Incoming model for creating a Billthemeshow"""
    # TODO: Add fields


class BillthemeshowOut(BaseModel):
    """Outgoing model for returning a Billthemeshow"""
    # TODO: Add fields


class BillthemeShowUpdate(BaseModel):
    """Update model for patching a Billthemeshow"""
    # TODO: Add fields


class BillthemeshowDb(BaseModel):
    """Internal DB representation for Billthemeshow"""
    # TODO: Add fields
