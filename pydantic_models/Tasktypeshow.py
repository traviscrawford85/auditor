from pydantic import BaseModel
from typing import Optional, List


class TasktypeShowIn(BaseModel):
    """Incoming model for creating a Tasktypeshow"""
    # TODO: Add fields


class TasktypeshowOut(BaseModel):
    """Outgoing model for returning a Tasktypeshow"""
    # TODO: Add fields


class TasktypeShowUpdate(BaseModel):
    """Update model for patching a Tasktypeshow"""
    # TODO: Add fields


class TasktypeshowDb(BaseModel):
    """Internal DB representation for Tasktypeshow"""
    # TODO: Add fields
