from pydantic import BaseModel


class TextsnippetIn(BaseModel):
    """Incoming model for creating a Textsnippet"""
    # TODO: Add fields


class TextsnippetOut(BaseModel):
    """Outgoing model for returning a Textsnippet"""
    # TODO: Add fields


class TextsnippetUpdate(BaseModel):
    """Update model for patching a Textsnippet"""
    # TODO: Add fields


class TextsnippetDb(BaseModel):
    """Internal DB representation for Textsnippet"""
    # TODO: Add fields
