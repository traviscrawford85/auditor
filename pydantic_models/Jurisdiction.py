from pydantic import BaseModel


class JurisdictionIn(BaseModel):
    """Incoming model for creating a Jurisdiction"""
    # TODO: Add fields


class JurisdictionOut(BaseModel):
    """Outgoing model for returning a Jurisdiction"""
    # TODO: Add fields


class JurisdictionUpdate(BaseModel):
    """Update model for patching a Jurisdiction"""
    # TODO: Add fields


class JurisdictionDb(BaseModel):
    """Internal DB representation for Jurisdiction"""
    # TODO: Add fields
