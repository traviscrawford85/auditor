from pydantic import BaseModel


class MyeventShowIn(BaseModel):
    """Incoming model for creating a Myeventshow"""
    # TODO: Add fields


class MyeventshowOut(BaseModel):
    """Outgoing model for returning a Myeventshow"""
    # TODO: Add fields


class MyeventShowUpdate(BaseModel):
    """Update model for patching a Myeventshow"""
    # TODO: Add fields


class MyeventshowDb(BaseModel):
    """Internal DB representation for Myeventshow"""
    # TODO: Add fields
