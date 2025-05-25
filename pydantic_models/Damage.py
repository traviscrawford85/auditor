from pydantic import BaseModel
from typing import Optional, List


class DamageIn(BaseModel):
    """Incoming model for creating a Damage"""
    # TODO: Add fields


class DamageOut(BaseModel):
    """Outgoing model for returning a Damage"""
    # TODO: Add fields


class DamageUpdate(BaseModel):
    """Update model for patching a Damage"""
    # TODO: Add fields


class DamageDb(BaseModel):
    """Internal DB representation for Damage"""
    # TODO: Add fields
