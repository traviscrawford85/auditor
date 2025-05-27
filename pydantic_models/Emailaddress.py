from pydantic import BaseModel


class EmailaddressIn(BaseModel):
    """Incoming model for creating a Emailaddress"""
    # TODO: Add fields


class EmailaddressOut(BaseModel):
    """Outgoing model for returning a Emailaddress"""
    # TODO: Add fields


class EmailaddressUpdate(BaseModel):
    """Update model for patching a Emailaddress"""
    # TODO: Add fields


class EmailaddressDb(BaseModel):
    """Internal DB representation for Emailaddress"""
    # TODO: Add fields
