from pydantic import BaseModel


class ConversationShowIn(BaseModel):
    """Incoming model for creating a Conversationshow"""
    # TODO: Add fields


class ConversationshowOut(BaseModel):
    """Outgoing model for returning a Conversationshow"""
    # TODO: Add fields


class ConversationShowUpdate(BaseModel):
    """Update model for patching a Conversationshow"""
    # TODO: Add fields


class ConversationshowDb(BaseModel):
    """Internal DB representation for Conversationshow"""
    # TODO: Add fields
