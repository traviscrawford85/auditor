from pydantic import BaseModel


class MyeventListIn(BaseModel):
    """Incoming model for creating a Myeventlist"""
    # TODO: Add fields


class MyeventlistOut(BaseModel):
    """Outgoing model for returning a Myeventlist"""
    # TODO: Add fields


class MyeventlistUpdate(BaseModel):
    """Update model for patching a Myeventlist"""
    # TODO: Add fields


class MyeventlistDb(BaseModel):
    """Internal DB representation for Myeventlist"""
    # TODO: Add fields
