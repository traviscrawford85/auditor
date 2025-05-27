from pydantic import BaseModel


class BillablematterShowIn(BaseModel):
    """Incoming model for creating a Billablemattershow"""
    # TODO: Add fields


class BillablemattershowOut(BaseModel):
    """Outgoing model for returning a Billablemattershow"""
    # TODO: Add fields


class BillablematterShowUpdate(BaseModel):
    """Update model for patching a Billablemattershow"""
    # TODO: Add fields


class BillablemattershowDb(BaseModel):
    """Internal DB representation for Billablemattershow"""
    # TODO: Add fields
