from pydantic import BaseModel


class JurisdictionListIn(BaseModel):
    """Incoming model for creating a Jurisdictionlist"""
    # TODO: Add fields


class JurisdictionlistOut(BaseModel):
    """Outgoing model for returning a Jurisdictionlist"""
    # TODO: Add fields


class JurisdictionlistUpdate(BaseModel):
    """Update model for patching a Jurisdictionlist"""
    # TODO: Add fields


class JurisdictionlistDb(BaseModel):
    """Internal DB representation for Jurisdictionlist"""
    # TODO: Add fields
