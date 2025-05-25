from pydantic import BaseModel
from typing import Optional, List


class GrantlistIn(BaseModel):
    """Incoming model for creating a Grantlist"""
    # TODO: Add fields


class GrantlistOut(BaseModel):
    """Outgoing model for returning a Grantlist"""
    # TODO: Add fields


class GrantlistUpdate(BaseModel):
    """Update model for patching a Grantlist"""
    # TODO: Add fields


class GrantlistDb(BaseModel):
    """Internal DB representation for Grantlist"""
    # TODO: Add fields
