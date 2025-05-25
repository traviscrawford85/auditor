from pydantic import BaseModel
from typing import Optional, List


class GrouplistIn(BaseModel):
    """Incoming model for creating a Grouplist"""
    # TODO: Add fields


class GrouplistOut(BaseModel):
    """Outgoing model for returning a Grouplist"""
    # TODO: Add fields


class GrouplistUpdate(BaseModel):
    """Update model for patching a Grouplist"""
    # TODO: Add fields


class GrouplistDb(BaseModel):
    """Internal DB representation for Grouplist"""
    # TODO: Add fields
