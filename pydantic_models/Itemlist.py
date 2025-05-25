from pydantic import BaseModel
from typing import Optional, List


class ItemlistIn(BaseModel):
    """Incoming model for creating a Itemlist"""
    # TODO: Add fields


class ItemlistOut(BaseModel):
    """Outgoing model for returning a Itemlist"""
    # TODO: Add fields


class ItemlistUpdate(BaseModel):
    """Update model for patching a Itemlist"""
    # TODO: Add fields


class ItemlistDb(BaseModel):
    """Internal DB representation for Itemlist"""
    # TODO: Add fields
