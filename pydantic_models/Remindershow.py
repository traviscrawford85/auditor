from pydantic import BaseModel
from typing import Optional, List


class RemindershowIn(BaseModel):
    """Incoming model for creating a Remindershow"""
    # TODO: Add fields


class RemindershowOut(BaseModel):
    """Outgoing model for returning a Remindershow"""
    # TODO: Add fields


class RemindershowUpdate(BaseModel):
    """Update model for patching a Remindershow"""
    # TODO: Add fields


class RemindershowDb(BaseModel):
    """Internal DB representation for Remindershow"""
    # TODO: Add fields
