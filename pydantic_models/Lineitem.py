from pydantic import BaseModel


class LineitemIn(BaseModel):
    """Incoming model for creating a Lineitem"""
    # TODO: Add fields


class LineitemOut(BaseModel):
    """Outgoing model for returning a Lineitem"""
    # TODO: Add fields


class LineitemUpdate(BaseModel):
    """Update model for patching a Lineitem"""
    # TODO: Add fields


class LineitemDb(BaseModel):
    """Internal DB representation for Lineitem"""
    # TODO: Add fields
