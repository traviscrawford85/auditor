from pydantic import BaseModel
from typing import Optional, List


class NoteListIn(BaseModel):
    """Incoming model for creating a Notelist"""
    # TODO: Add fields


class NotelistOut(BaseModel):
    """Outgoing model for returning a Notelist"""
    # TODO: Add fields


class NotelistUpdate(BaseModel):
    """Update model for patching a Notelist"""
    # TODO: Add fields


class NotelistDb(BaseModel):
    """Internal DB representation for Notelist"""
    # TODO: Add fields
