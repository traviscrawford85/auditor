from pydantic import BaseModel


class EmailaddressListIn(BaseModel):
    """Incoming model for creating a Emailaddresslist"""
    # TODO: Add fields


class EmailaddresslistOut(BaseModel):
    """Outgoing model for returning a Emailaddresslist"""
    # TODO: Add fields


class EmailaddresslistUpdate(BaseModel):
    """Update model for patching a Emailaddresslist"""
    # TODO: Add fields


class EmailaddresslistDb(BaseModel):
    """Internal DB representation for Emailaddresslist"""
    # TODO: Add fields
