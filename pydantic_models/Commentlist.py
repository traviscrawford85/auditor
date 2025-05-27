from pydantic import BaseModel


class CommentListIn(BaseModel):
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
