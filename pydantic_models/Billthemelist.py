from pydantic import BaseModel


class BillthemeListIn(BaseModel):
    """Incoming model for creating a Billthemelist"""
    # TODO: Add fields


class BillthemelistOut(BaseModel):
    """Outgoing model for returning a Billthemelist"""
    # TODO: Add fields


class BillthemelistUpdate(BaseModel):
    """Update model for patching a Billthemelist"""
    # TODO: Add fields


class BillthemelistDb(BaseModel):
    """Internal DB representation for Billthemelist"""
    # TODO: Add fields
