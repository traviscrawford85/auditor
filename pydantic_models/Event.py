from pydantic import BaseModel
from typing import Optional, List


class EventIn(BaseModel):
    """Incoming model for creating a Event"""
    # TODO: Add fields


class EventOut(BaseModel):
    """Outgoing model for returning a Event"""
    # TODO: Add fields


class EventUpdate(BaseModel):
    """Update model for patching a Event"""
    # TODO: Add fields


class EventDb(BaseModel):
    """Internal DB representation for Event"""
    # TODO: Add fields
