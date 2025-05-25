from pydantic import BaseModel
from typing import Optional, List


class UserIn(BaseModel):
    """Incoming model for creating a User"""
    # TODO: Add fields


class UserOut(BaseModel):
    """Outgoing model for returning a User"""
    # TODO: Add fields


class UserUpdate(BaseModel):
    """Update model for patching a User"""
    # TODO: Add fields


class UserDb(BaseModel):
    """Internal DB representation for User"""
    # TODO: Add fields
