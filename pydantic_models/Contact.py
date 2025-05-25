from pydantic import BaseModel
from typing import Optional, List


class ContactIn(BaseModel):
    """Incoming model for creating a Contact"""
    # TODO: Add fields


class ContactOut(BaseModel):
    """Outgoing model for returning a Contact"""
    # TODO: Add fields


class ContactUpdate(BaseModel):
    """Update model for patching a Contact"""
    # TODO: Add fields


class ContactDb(BaseModel):
    """Internal DB representation for Contact"""
    # TODO: Add fields
