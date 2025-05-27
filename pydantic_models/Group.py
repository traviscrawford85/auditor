from pydantic import BaseModel


class GroupIn(BaseModel):
    """Incoming model for creating a Group"""
    # TODO: Add fields


class GroupOut(BaseModel):
    """Outgoing model for returning a Group"""
    # TODO: Add fields


class GroupUpdate(BaseModel):
    """Update model for patching a Group"""
    # TODO: Add fields


class GroupDb(BaseModel):
    """Internal DB representation for Group"""
    # TODO: Add fields
