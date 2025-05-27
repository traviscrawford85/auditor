from pydantic import BaseModel


class TimerIn(BaseModel):
    """Incoming model for creating a Timer"""
    # TODO: Add fields


class TimerOut(BaseModel):
    """Outgoing model for returning a Timer"""
    # TODO: Add fields


class TimerUpdate(BaseModel):
    """Update model for patching a Timer"""
    # TODO: Add fields


class TimerDb(BaseModel):
    """Internal DB representation for Timer"""
    # TODO: Add fields
