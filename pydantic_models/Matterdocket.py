from pydantic import BaseModel


class MatterdocketIn(BaseModel):
    """Incoming model for creating a Matterdocket"""
    # TODO: Add fields


class MatterdocketOut(BaseModel):
    """Outgoing model for returning a Matterdocket"""
    # TODO: Add fields


class MatterdocketUpdate(BaseModel):
    """Update model for patching a Matterdocket"""
    # TODO: Add fields


class MatterdocketDb(BaseModel):
    """Internal DB representation for Matterdocket"""
    # TODO: Add fields
