from pydantic import BaseModel
from typing import Optional, List


class MattershowIn(BaseModel):
    """Incoming model for creating a Mattershow"""
    # TODO: Add fields


class MattershowOut(BaseModel):
    """Outgoing model for returning a Mattershow"""
    # TODO: Add fields


class MattershowUpdate(BaseModel):
    """Update model for patching a Mattershow"""
    # TODO: Add fields


class MattershowDb(BaseModel):
    """Internal DB representation for Mattershow"""
    # TODO: Add fields
