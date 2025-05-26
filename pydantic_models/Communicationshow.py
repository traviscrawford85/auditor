from pydantic import BaseModel
from typing import Optional, List


class CommunicationShowIn(BaseModel):
    """Incoming model for creating a Communicationshow"""
    # TODO: Add fields


class CommunicationshowOut(BaseModel):
    """Outgoing model for returning a Communicationshow"""
    # TODO: Add fields


class CommunicationShowUpdate(BaseModel):
    """Update model for patching a Communicationshow"""
    # TODO: Add fields


class CommunicationshowDb(BaseModel):
    """Internal DB representation for Communicationshow"""
    # TODO: Add fields
