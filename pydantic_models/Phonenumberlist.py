from pydantic import BaseModel
from typing import Optional, List


class PhonenumberListIn(BaseModel):
    """Incoming model for creating a Phonenumberlist"""
    # TODO: Add fields


class PhonenumberlistOut(BaseModel):
    """Outgoing model for returning a Phonenumberlist"""
    # TODO: Add fields


class PhonenumberlistUpdate(BaseModel):
    """Update model for patching a Phonenumberlist"""
    # TODO: Add fields


class PhonenumberlistDb(BaseModel):
    """Internal DB representation for Phonenumberlist"""
    # TODO: Add fields
