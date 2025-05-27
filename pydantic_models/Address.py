from pydantic import BaseModel


class AddressIn(BaseModel):
    """Incoming model for creating a Address"""
    # TODO: Add fields


class AddressOut(BaseModel):
    """Outgoing model for returning a Address"""
    # TODO: Add fields


class AddressUpdate(BaseModel):
    """Update model for patching a Address"""
    # TODO: Add fields


class AddressDb(BaseModel):
    """Internal DB representation for Address"""
    # TODO: Add fields
