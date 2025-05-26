from pydantic import BaseModel
from typing import Optional, List


class ContactShowIn(BaseModel):
    """Incoming model for creating a Contactshow"""
    # TODO: Add fields


class ContactshowOut(BaseModel):
    """Outgoing model for returning a Contactshow"""
    # TODO: Add fields


class ContactShowUpdate(BaseModel):
    """Update model for patching a Contactshow"""
    # TODO: Add fields


class ContactshowDb(BaseModel):
    """Internal DB representation for Contactshow"""
    # TODO: Add fields
