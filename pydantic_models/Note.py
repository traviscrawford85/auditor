from pydantic import BaseModel
from typing import Optional, List


class NoteIn(BaseModel):
    """Incoming model for creating a Note"""
    # TODO: Add fields


class NoteOut(BaseModel):
    """Outgoing model for returning a Note"""
    # TODO: Add fields


class NoteUpdate(BaseModel):
    """Update model for patching a Note"""
    # TODO: Add fields


class NoteDb(BaseModel):
    """Internal DB representation for Note"""
    # TODO: Add fields
