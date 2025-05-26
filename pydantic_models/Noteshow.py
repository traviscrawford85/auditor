from pydantic import BaseModel
from typing import Optional, List


class NoteShowIn(BaseModel):
    """Incoming model for creating a Noteshow"""
    # TODO: Add fields


class NoteshowOut(BaseModel):
    """Outgoing model for returning a Noteshow"""
    # TODO: Add fields


class NoteShowUpdate(BaseModel):
    """Update model for patching a Noteshow"""
    # TODO: Add fields


class NoteshowDb(BaseModel):
    """Internal DB representation for Noteshow"""
    # TODO: Add fields
