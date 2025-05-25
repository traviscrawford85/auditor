from pydantic import BaseModel
from typing import Optional, List


class ItemIn(BaseModel):
    """Incoming model for creating a Item"""
    # TODO: Add fields


class ItemOut(BaseModel):
    """Outgoing model for returning a Item"""
    # TODO: Add fields


class ItemUpdate(BaseModel):
    """Update model for patching a Item"""
    # TODO: Add fields


class ItemDb(BaseModel):
    """Internal DB representation for Item"""
    # TODO: Add fields
