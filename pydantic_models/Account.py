from pydantic import BaseModel
from typing import Optional, List


class AccountIn(BaseModel):
    """Incoming model for creating a Account"""
    # TODO: Add fields


class AccountOut(BaseModel):
    """Outgoing model for returning a Account"""
    # TODO: Add fields


class AccountUpdate(BaseModel):
    """Update model for patching a Account"""
    # TODO: Add fields


class AccountDb(BaseModel):
    """Internal DB representation for Account"""
    # TODO: Add fields
