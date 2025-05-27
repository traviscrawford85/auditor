from pydantic import BaseModel


class MatterIn(BaseModel):
    """Incoming model for creating a Matter"""
    # TODO: Add fields


class MatterOut(BaseModel):
    """Outgoing model for returning a Matter"""
    # TODO: Add fields


class MatterUpdate(BaseModel):
    """Update model for patching a Matter"""
    # TODO: Add fields


class MatterDb(BaseModel):
    """Internal DB representation for Matter"""
    # TODO: Add fields
