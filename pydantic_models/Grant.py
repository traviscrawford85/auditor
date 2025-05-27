from pydantic import BaseModel


class GrantIn(BaseModel):
    """Incoming model for creating a Grant"""
    # TODO: Add fields


class GrantOut(BaseModel):
    """Outgoing model for returning a Grant"""
    # TODO: Add fields


class GrantUpdate(BaseModel):
    """Update model for patching a Grant"""
    # TODO: Add fields


class GrantDb(BaseModel):
    """Internal DB representation for Grant"""
    # TODO: Add fields
