from pydantic import BaseModel
from typing import Optional, List


class GrantShowIn(BaseModel):
    """Incoming model for creating a Grantshow"""
    # TODO: Add fields


class GrantshowOut(BaseModel):
    """Outgoing model for returning a Grantshow"""
    # TODO: Add fields


class GrantShowUpdate(BaseModel):
    """Update model for patching a Grantshow"""
    # TODO: Add fields


class GrantshowDb(BaseModel):
    """Internal DB representation for Grantshow"""
    # TODO: Add fields
