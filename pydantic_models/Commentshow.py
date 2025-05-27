from pydantic import BaseModel


class CommentShowIn(BaseModel):
    """Incoming model for creating a Commentshow"""
    # TODO: Add fields


class CommentshowOut(BaseModel):
    """Outgoing model for returning a Commentshow"""
    # TODO: Add fields


class CommentShowUpdate(BaseModel):
    """Update model for patching a Commentshow"""
    # TODO: Add fields


class CommentshowDb(BaseModel):
    """Internal DB representation for Commentshow"""
    # TODO: Add fields
