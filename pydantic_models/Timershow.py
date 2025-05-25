from pydantic import BaseModel
from typing import Optional, List


class TimershowIn(BaseModel):
    """Incoming model for creating a Timershow"""
    # TODO: Add fields


class TimershowOut(BaseModel):
    """Outgoing model for returning a Timershow"""
    # TODO: Add fields


class TimershowUpdate(BaseModel):
    """Update model for patching a Timershow"""
    # TODO: Add fields


class TimershowDb(BaseModel):
    """Internal DB representation for Timershow"""
    # TODO: Add fields
