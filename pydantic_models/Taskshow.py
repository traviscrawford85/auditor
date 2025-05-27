from pydantic import BaseModel


class TaskShowIn(BaseModel):
    """Incoming model for creating a Taskshow"""
    # TODO: Add fields


class TaskshowOut(BaseModel):
    """Outgoing model for returning a Taskshow"""
    # TODO: Add fields


class TaskShowUpdate(BaseModel):
    """Update model for patching a Taskshow"""
    # TODO: Add fields


class TaskshowDb(BaseModel):
    """Internal DB representation for Taskshow"""
    # TODO: Add fields
