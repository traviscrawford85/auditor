from pydantic import BaseModel


class CommentIn(BaseModel):
    """Incoming model for creating a Comment"""
    # TODO: Add fields


class CommentOut(BaseModel):
    """Outgoing model for returning a Comment"""
    # TODO: Add fields


class CommentUpdate(BaseModel):
    """Update model for patching a Comment"""
    # TODO: Add fields


class CommentDb(BaseModel):
    """Internal DB representation for Comment"""
    # TODO: Add fields
