from pydantic import BaseModel
from typing import Optional, List


class ConversationmessageIn(BaseModel):
    """Incoming model for creating a Conversationmessage"""
    # TODO: Add fields


class ConversationmessageOut(BaseModel):
    """Outgoing model for returning a Conversationmessage"""
    # TODO: Add fields


class ConversationmessageUpdate(BaseModel):
    """Update model for patching a Conversationmessage"""
    # TODO: Add fields


class ConversationmessageDb(BaseModel):
    """Internal DB representation for Conversationmessage"""
    # TODO: Add fields
