from pydantic import BaseModel


class LineitemListIn(BaseModel):
    """Incoming model for creating a Lineitemlist"""
    # TODO: Add fields


class LineitemlistOut(BaseModel):
    """Outgoing model for returning a Lineitemlist"""
    # TODO: Add fields


class LineitemlistUpdate(BaseModel):
    """Update model for patching a Lineitemlist"""
    # TODO: Add fields


class LineitemlistDb(BaseModel):
    """Internal DB representation for Lineitemlist"""
    # TODO: Add fields
