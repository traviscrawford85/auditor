from pydantic import BaseModel
from typing import Optional, List


class TrustlineitemIn(BaseModel):
    """Incoming model for creating a Trustlineitem"""
    # TODO: Add fields


class TrustlineitemOut(BaseModel):
    """Outgoing model for returning a Trustlineitem"""
    # TODO: Add fields


class TrustlineitemUpdate(BaseModel):
    """Update model for patching a Trustlineitem"""
    # TODO: Add fields


class TrustlineitemDb(BaseModel):
    """Internal DB representation for Trustlineitem"""
    # TODO: Add fields
