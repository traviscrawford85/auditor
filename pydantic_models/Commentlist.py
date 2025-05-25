from pydantic import BaseModel
from typing import Optional, List


class CommentlistIn(BaseModel):
    """Incoming model for creating a Commentlist"""
    # TODO: Add fields


class CommentlistOut(BaseModel):
    """Outgoing model for returning a Commentlist"""
    # TODO: Add fields


class CommentlistUpdate(BaseModel):
    """Update model for patching a Commentlist"""
    # TODO: Add fields


class CommentlistDb(BaseModel):
    """Internal DB representation for Commentlist"""
    # TODO: Add fields
