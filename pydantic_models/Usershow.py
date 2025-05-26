from pydantic import BaseModel
from typing import Optional, List


class UserShowIn(BaseModel):
    """Incoming model for creating a Usershow"""
    # TODO: Add fields


class UsershowOut(BaseModel):
    """Outgoing model for returning a Usershow"""
    # TODO: Add fields


class UserShowUpdate(BaseModel):
    """Update model for patching a Usershow"""
    # TODO: Add fields


class UsershowDb(BaseModel):
    """Internal DB representation for Usershow"""
    # TODO: Add fields
