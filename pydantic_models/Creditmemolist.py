from pydantic import BaseModel
from typing import Optional, List


class CreditmemoListIn(BaseModel):
    """Incoming model for creating a Creditmemolist"""
    # TODO: Add fields


class CreditmemolistOut(BaseModel):
    """Outgoing model for returning a Creditmemolist"""
    # TODO: Add fields


class CreditmemolistUpdate(BaseModel):
    """Update model for patching a Creditmemolist"""
    # TODO: Add fields


class CreditmemolistDb(BaseModel):
    """Internal DB representation for Creditmemolist"""
    # TODO: Add fields
