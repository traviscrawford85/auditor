from pydantic import BaseModel


class MyeventIn(BaseModel):
    """Incoming model for creating a Myevent"""
    # TODO: Add fields


class MyeventOut(BaseModel):
    """Outgoing model for returning a Myevent"""
    # TODO: Add fields


class MyeventUpdate(BaseModel):
    """Update model for patching a Myevent"""
    # TODO: Add fields


class MyeventDb(BaseModel):
    """Internal DB representation for Myevent"""
    # TODO: Add fields
