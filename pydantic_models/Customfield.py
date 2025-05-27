from pydantic import BaseModel


class CustomfieldIn(BaseModel):
    """Incoming model for creating a Customfield"""
    # TODO: Add fields


class CustomfieldOut(BaseModel):
    """Outgoing model for returning a Customfield"""
    # TODO: Add fields


class CustomfieldUpdate(BaseModel):
    """Update model for patching a Customfield"""
    # TODO: Add fields


class CustomfieldDb(BaseModel):
    """Internal DB representation for Customfield"""
    # TODO: Add fields
