from pydantic import BaseModel


class ConversationmembershipIn(BaseModel):
    """Incoming model for creating a Conversationmembership"""
    # TODO: Add fields


class ConversationmembershipOut(BaseModel):
    """Outgoing model for returning a Conversationmembership"""
    # TODO: Add fields


class ConversationmembershipUpdate(BaseModel):
    """Update model for patching a Conversationmembership"""
    # TODO: Add fields


class ConversationmembershipDb(BaseModel):
    """Internal DB representation for Conversationmembership"""
    # TODO: Add fields
