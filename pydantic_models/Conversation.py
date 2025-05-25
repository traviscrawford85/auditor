from pydantic import BaseModel
from typing import Optional, List


class ConversationIn(BaseModel):
    """Incoming model for creating a Conversation"""
    # TODO: Add fields


class ConversationOut(BaseModel):
    """Outgoing model for returning a Conversation"""
    # TODO: Add fields


class ConversationUpdate(BaseModel):
    """Update model for patching a Conversation"""
    # TODO: Add fields


class ConversationDb(BaseModel):
    """Internal DB representation for Conversation"""
    # TODO: Add fields
