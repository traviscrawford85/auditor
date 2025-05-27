from pydantic import BaseModel


class CommunicationIn(BaseModel):
    """Incoming model for creating a Communication"""
    # TODO: Add fields


class CommunicationOut(BaseModel):
    """Outgoing model for returning a Communication"""
    # TODO: Add fields


class CommunicationUpdate(BaseModel):
    """Update model for patching a Communication"""
    # TODO: Add fields


class CommunicationDb(BaseModel):
    """Internal DB representation for Communication"""
    # TODO: Add fields
