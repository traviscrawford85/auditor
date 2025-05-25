from pydantic import BaseModel
from typing import Optional, List


class TasktypeIn(BaseModel):
    """Incoming model for creating a Tasktype"""
    # TODO: Add fields


class TasktypeOut(BaseModel):
    """Outgoing model for returning a Tasktype"""
    # TODO: Add fields


class TasktypeUpdate(BaseModel):
    """Update model for patching a Tasktype"""
    # TODO: Add fields


class TasktypeDb(BaseModel):
    """Internal DB representation for Tasktype"""
    # TODO: Add fields
