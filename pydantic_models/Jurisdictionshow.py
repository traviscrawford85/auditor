from pydantic import BaseModel
from typing import Optional, List


class JurisdictionShowIn(BaseModel):
    """Incoming model for creating a Jurisdictionshow"""
    # TODO: Add fields


class JurisdictionshowOut(BaseModel):
    """Outgoing model for returning a Jurisdictionshow"""
    # TODO: Add fields


class JurisdictionShowUpdate(BaseModel):
    """Update model for patching a Jurisdictionshow"""
    # TODO: Add fields


class JurisdictionshowDb(BaseModel):
    """Internal DB representation for Jurisdictionshow"""
    # TODO: Add fields
