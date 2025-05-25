from pydantic import BaseModel
from typing import Optional, List


class ClientshowIn(BaseModel):
    """Incoming model for creating a Clientshow"""
    # TODO: Add fields


class ClientshowOut(BaseModel):
    """Outgoing model for returning a Clientshow"""
    # TODO: Add fields


class ClientshowUpdate(BaseModel):
    """Update model for patching a Clientshow"""
    # TODO: Add fields


class ClientshowDb(BaseModel):
    """Internal DB representation for Clientshow"""
    # TODO: Add fields
