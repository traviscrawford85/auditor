from pydantic import BaseModel
from typing import Optional, List


class GroupShowIn(BaseModel):
    """Incoming model for creating a Groupshow"""
    # TODO: Add fields


class GroupshowOut(BaseModel):
    """Outgoing model for returning a Groupshow"""
    # TODO: Add fields


class GroupShowUpdate(BaseModel):
    """Update model for patching a Groupshow"""
    # TODO: Add fields


class GroupshowDb(BaseModel):
    """Internal DB representation for Groupshow"""
    # TODO: Add fields
