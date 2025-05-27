from pydantic import BaseModel


class BillListIn(BaseModel):
    """Incoming model for creating a Billlist"""
    # TODO: Add fields


class BilllistOut(BaseModel):
    """Outgoing model for returning a Billlist"""
    # TODO: Add fields


class BilllistUpdate(BaseModel):
    """Update model for patching a Billlist"""
    # TODO: Add fields


class BilllistDb(BaseModel):
    """Internal DB representation for Billlist"""
    # TODO: Add fields
