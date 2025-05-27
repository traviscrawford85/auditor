from pydantic import BaseModel


class CustomactionShowIn(BaseModel):
    """Incoming model for creating a Customactionshow"""
    # TODO: Add fields


class CustomactionshowOut(BaseModel):
    """Outgoing model for returning a Customactionshow"""
    # TODO: Add fields


class CustomactionShowUpdate(BaseModel):
    """Update model for patching a Customactionshow"""
    # TODO: Add fields


class CustomactionshowDb(BaseModel):
    """Internal DB representation for Customactionshow"""
    # TODO: Add fields
