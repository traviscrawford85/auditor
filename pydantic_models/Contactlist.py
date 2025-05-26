from pydantic import BaseModel
from typing import Optional, List


class ContactListIn(BaseModel):
    """Incoming model for creating a Contactlist"""
    # TODO: Add fields


class ContactlistOut(BaseModel):
    """Outgoing model for returning a Contactlist"""
    # TODO: Add fields


class ContactlistUpdate(BaseModel):
    """Update model for patching a Contactlist"""
    # TODO: Add fields


class ContactlistDb(BaseModel):
    """Internal DB representation for Contactlist"""
    # TODO: Add fields
