from pydantic import BaseModel


class BillthemeIn(BaseModel):
    """Incoming model for creating a Billtheme"""
    # TODO: Add fields


class BillthemeOut(BaseModel):
    """Outgoing model for returning a Billtheme"""
    # TODO: Add fields


class BillthemeUpdate(BaseModel):
    """Update model for patching a Billtheme"""
    # TODO: Add fields


class BillthemeDb(BaseModel):
    """Internal DB representation for Billtheme"""
    # TODO: Add fields
