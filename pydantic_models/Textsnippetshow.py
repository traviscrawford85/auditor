from pydantic import BaseModel


class TextsnippetShowIn(BaseModel):
    """Incoming model for creating a Textsnippetshow"""
    # TODO: Add fields


class TextsnippetshowOut(BaseModel):
    """Outgoing model for returning a Textsnippetshow"""
    # TODO: Add fields


class TextsnippetShowUpdate(BaseModel):
    """Update model for patching a Textsnippetshow"""
    # TODO: Add fields


class TextsnippetshowDb(BaseModel):
    """Internal DB representation for Textsnippetshow"""
    # TODO: Add fields
