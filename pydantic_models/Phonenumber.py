from pydantic import BaseModel


class PhonenumberIn(BaseModel):
    """Incoming model for creating a Phonenumber"""
    # TODO: Add fields


class PhonenumberOut(BaseModel):
    """Outgoing model for returning a Phonenumber"""
    # TODO: Add fields


class PhonenumberUpdate(BaseModel):
    """Update model for patching a Phonenumber"""
    # TODO: Add fields


class PhonenumberDb(BaseModel):
    """Internal DB representation for Phonenumber"""
    # TODO: Add fields
