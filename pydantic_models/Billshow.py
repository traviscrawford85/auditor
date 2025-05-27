from pydantic import BaseModel


class BillShowIn(BaseModel):
    """Incoming model for creating a Billshow"""
    # TODO: Add fields


class BillshowOut(BaseModel):
    """Outgoing model for returning a Billshow"""
    # TODO: Add fields


class BillShowUpdate(BaseModel):
    """Update model for patching a Billshow"""
    # TODO: Add fields


class BillshowDb(BaseModel):
    """Internal DB representation for Billshow"""
    # TODO: Add fields
