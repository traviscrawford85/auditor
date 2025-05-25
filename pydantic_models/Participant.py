from pydantic import BaseModel
from typing import Optional, List


class ParticipantIn(BaseModel):
    """Incoming model for creating a Participant"""
    # TODO: Add fields


class ParticipantOut(BaseModel):
    """Outgoing model for returning a Participant"""
    # TODO: Add fields


class ParticipantUpdate(BaseModel):
    """Update model for patching a Participant"""
    # TODO: Add fields


class ParticipantDb(BaseModel):
    """Internal DB representation for Participant"""
    # TODO: Add fields
