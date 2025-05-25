from pydantic import BaseModel
from typing import Optional, List


class ClientIn(BaseModel):
    """Incoming model for creating a Client"""
    # TODO: Add fields


class ClientOut(BaseModel):
    """Outgoing model for returning a Client"""
    # TODO: Add fields


class ClientUpdate(BaseModel):
    """Update model for patching a Client"""
    # TODO: Add fields


class ClientDb(BaseModel):
    """Internal DB representation for Client"""
    # TODO: Add fields
