from pydantic import BaseModel


class MatterstageListIn(BaseModel):
    """Incoming model for creating a Matterstagelist"""
    # TODO: Add fields


class MatterstagelistOut(BaseModel):
    """Outgoing model for returning a Matterstagelist"""
    # TODO: Add fields


class MatterstagelistUpdate(BaseModel):
    """Update model for patching a Matterstagelist"""
    # TODO: Add fields


class MatterstagelistDb(BaseModel):
    """Internal DB representation for Matterstagelist"""
    # TODO: Add fields
