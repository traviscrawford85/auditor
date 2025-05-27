from pydantic import BaseModel


class BillableclientIn(BaseModel):
    """Incoming model for creating a Billableclient"""
    # TODO: Add fields


class BillableclientOut(BaseModel):
    """Outgoing model for returning a Billableclient"""
    # TODO: Add fields


class BillableclientUpdate(BaseModel):
    """Update model for patching a Billableclient"""
    # TODO: Add fields


class BillableclientDb(BaseModel):
    """Internal DB representation for Billableclient"""
    # TODO: Add fields
