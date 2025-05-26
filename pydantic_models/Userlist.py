from pydantic import BaseModel
from typing import Optional, List


class UserListIn(BaseModel):
    """Incoming model for creating a Userlist"""
    # TODO: Add fields


class UserlistOut(BaseModel):
    """Outgoing model for returning a Userlist"""
    # TODO: Add fields


class UserlistUpdate(BaseModel):
    """Update model for patching a Userlist"""
    # TODO: Add fields


class UserlistDb(BaseModel):
    """Internal DB representation for Userlist"""
    # TODO: Add fields
