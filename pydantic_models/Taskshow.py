from pydantic import BaseModel
from typing import Optional, List


class TaskshowIn(BaseModel):
    """Incoming model for creating a Taskshow"""
    # TODO: Add fields


class TaskshowOut(BaseModel):
    """Outgoing model for returning a Taskshow"""
    # TODO: Add fields


class TaskshowUpdate(BaseModel):
    """Update model for patching a Taskshow"""
    # TODO: Add fields


class TaskshowDb(BaseModel):
    """Internal DB representation for Taskshow"""
    # TODO: Add fields
