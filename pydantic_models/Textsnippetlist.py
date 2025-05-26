from pydantic import BaseModel
from typing import Optional, List


class TextsnippetListIn(BaseModel):
    """Incoming model for creating a Textsnippetlist"""
    # TODO: Add fields


class TextsnippetlistOut(BaseModel):
    """Outgoing model for returning a Textsnippetlist"""
    # TODO: Add fields


class TextsnippetlistUpdate(BaseModel):
    """Update model for patching a Textsnippetlist"""
    # TODO: Add fields


class TextsnippetlistDb(BaseModel):
    """Internal DB representation for Textsnippetlist"""
    # TODO: Add fields
