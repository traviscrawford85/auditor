from pydantic import BaseModel


class TimerShowIn(BaseModel):
    """Incoming model for creating a Timershow"""
    # TODO: Add fields


class TimershowOut(BaseModel):
    """Outgoing model for returning a Timershow"""
    # TODO: Add fields


class TimerShowUpdate(BaseModel):
    """Update model for patching a Timershow"""
    # TODO: Add fields


class TimershowDb(BaseModel):
    """Internal DB representation for Timershow"""
    # TODO: Add fields
