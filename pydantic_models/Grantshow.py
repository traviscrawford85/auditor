from pydantic import BaseModel
from typing import Optional, List


class GrantshowIn(BaseModel):
    """Incoming model for creating a Grantshow"""
    # TODO: Add fields


class GrantshowOut(BaseModel):
    """Outgoing model for returning a Grantshow"""
    # TODO: Add fields


class GrantshowUpdate(BaseModel):
    """Update model for patching a Grantshow"""
    # TODO: Add fields


class GrantshowDb(BaseModel):
    """Internal DB representation for Grantshow"""
    # TODO: Add fields
