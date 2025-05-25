from pydantic import BaseModel
from typing import Optional, List


class ActivityIn(BaseModel):
    """Incoming model for creating a Activity"""
    # TODO: Add fields


class ActivityOut(BaseModel):
    """Outgoing model for returning a Activity"""
    # TODO: Add fields


class ActivityUpdate(BaseModel):
    """Update model for patching a Activity"""
    # TODO: Add fields


class ActivityDb(BaseModel):
    """Internal DB representation for Activity"""
    # TODO: Add fields
