from pydantic import BaseModel
from typing import Optional, List


class FolderShowIn(BaseModel):
    """Incoming model for creating a Foldershow"""
    # TODO: Add fields


class FoldershowOut(BaseModel):
    """Outgoing model for returning a Foldershow"""
    # TODO: Add fields


class FolderShowUpdate(BaseModel):
    """Update model for patching a Foldershow"""
    # TODO: Add fields


class FoldershowDb(BaseModel):
    """Internal DB representation for Foldershow"""
    # TODO: Add fields
