from pydantic import BaseModel
from typing import Optional, List


class TaskIn(BaseModel):
    """Incoming model for creating a Task"""
    # TODO: Add fields


class TaskOut(BaseModel):
    """Outgoing model for returning a Task"""
    # TODO: Add fields


class TaskUpdate(BaseModel):
    """Update model for patching a Task"""
    # TODO: Add fields


class TaskDb(BaseModel):
    """Internal DB representation for Task"""
    # TODO: Add fields
