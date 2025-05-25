from pydantic import BaseModel
from typing import Optional, List


class CustomactionIn(BaseModel):
    """Incoming model for creating a Customaction"""
    # TODO: Add fields


class CustomactionOut(BaseModel):
    """Outgoing model for returning a Customaction"""
    # TODO: Add fields


class CustomactionUpdate(BaseModel):
    """Update model for patching a Customaction"""
    # TODO: Add fields


class CustomactionDb(BaseModel):
    """Internal DB representation for Customaction"""
    # TODO: Add fields
