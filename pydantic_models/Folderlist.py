from pydantic import BaseModel
from typing import Optional, List


class FolderListIn(BaseModel):
    """Incoming model for creating a Folderlist"""
    # TODO: Add fields


class FolderlistOut(BaseModel):
    """Outgoing model for returning a Folderlist"""
    # TODO: Add fields


class FolderlistUpdate(BaseModel):
    """Update model for patching a Folderlist"""
    # TODO: Add fields


class FolderlistDb(BaseModel):
    """Internal DB representation for Folderlist"""
    # TODO: Add fields
