from pydantic import BaseModel
from typing import Optional, List


class MatterstageIn(BaseModel):
    """Incoming model for creating a Matterstage"""
    # TODO: Add fields


class MatterstageOut(BaseModel):
    """Outgoing model for returning a Matterstage"""
    # TODO: Add fields


class MatterstageUpdate(BaseModel):
    """Update model for patching a Matterstage"""
    # TODO: Add fields


class MatterstageDb(BaseModel):
    """Internal DB representation for Matterstage"""
    # TODO: Add fields
