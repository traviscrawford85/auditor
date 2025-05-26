from pydantic import BaseModel
from typing import Optional, List


class CommunicationListIn(BaseModel):
    """Incoming model for creating a Communicationlist"""
    # TODO: Add fields


class CommunicationlistOut(BaseModel):
    """Outgoing model for returning a Communicationlist"""
    # TODO: Add fields


class CommunicationlistUpdate(BaseModel):
    """Update model for patching a Communicationlist"""
    # TODO: Add fields


class CommunicationlistDb(BaseModel):
    """Internal DB representation for Communicationlist"""
    # TODO: Add fields
