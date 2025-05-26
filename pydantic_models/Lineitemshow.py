from pydantic import BaseModel
from typing import Optional, List


class LineitemShowIn(BaseModel):
    """Incoming model for creating a Lineitemshow"""
    # TODO: Add fields


class LineitemshowOut(BaseModel):
    """Outgoing model for returning a Lineitemshow"""
    # TODO: Add fields


class LineitemShowUpdate(BaseModel):
    """Update model for patching a Lineitemshow"""
    # TODO: Add fields


class LineitemshowDb(BaseModel):
    """Internal DB representation for Lineitemshow"""
    # TODO: Add fields
