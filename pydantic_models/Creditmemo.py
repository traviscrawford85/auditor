from pydantic import BaseModel
from typing import Optional, List


class CreditmemoIn(BaseModel):
    """Incoming model for creating a Creditmemo"""
    # TODO: Add fields


class CreditmemoOut(BaseModel):
    """Outgoing model for returning a Creditmemo"""
    # TODO: Add fields


class CreditmemoUpdate(BaseModel):
    """Update model for patching a Creditmemo"""
    # TODO: Add fields


class CreditmemoDb(BaseModel):
    """Internal DB representation for Creditmemo"""
    # TODO: Add fields
