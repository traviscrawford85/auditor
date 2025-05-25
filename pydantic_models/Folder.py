from pydantic import BaseModel
from typing import Optional, List


class FolderIn(BaseModel):
    """Incoming model for creating a Folder"""
    # TODO: Add fields


class FolderOut(BaseModel):
    """Outgoing model for returning a Folder"""
    # TODO: Add fields


class FolderUpdate(BaseModel):
    """Update model for patching a Folder"""
    # TODO: Add fields


class FolderDb(BaseModel):
    """Internal DB representation for Folder"""
    # TODO: Add fields
