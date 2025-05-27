from pydantic import BaseModel


class ConversationListIn(BaseModel):
    """Incoming model for creating a Conversationlist"""
    # TODO: Add fields


class ConversationlistOut(BaseModel):
    """Outgoing model for returning a Conversationlist"""
    # TODO: Add fields


class ConversationlistUpdate(BaseModel):
    """Update model for patching a Conversationlist"""
    # TODO: Add fields


class ConversationlistDb(BaseModel):
    """Internal DB representation for Conversationlist"""
    # TODO: Add fields
