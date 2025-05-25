from pydantic import BaseModel
from typing import Optional, List


class MatterlistIn(BaseModel):
    """Incoming model for creating a Matterlist"""
    # TODO: Add fields


class MatterlistOut(BaseModel):
    """Outgoing model for returning a Matterlist"""
    # TODO: Add fields


class MatterlistUpdate(BaseModel):
    """Update model for patching a Matterlist"""
    # TODO: Add fields


class MatterlistDb(BaseModel):
    """Internal DB representation for Matterlist"""
    # TODO: Add fields
