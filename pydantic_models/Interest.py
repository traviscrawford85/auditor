from pydantic import BaseModel
from typing import Optional, List


class InterestIn(BaseModel):
    """Incoming model for creating a Interest"""
    # TODO: Add fields


class InterestOut(BaseModel):
    """Outgoing model for returning a Interest"""
    # TODO: Add fields


class InterestUpdate(BaseModel):
    """Update model for patching a Interest"""
    # TODO: Add fields


class InterestDb(BaseModel):
    """Internal DB representation for Interest"""
    # TODO: Add fields
