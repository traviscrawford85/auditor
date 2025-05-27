from pydantic import BaseModel


class CreditmemoShowIn(BaseModel):
    """Incoming model for creating a Creditmemoshow"""
    # TODO: Add fields


class CreditmemoshowOut(BaseModel):
    """Outgoing model for returning a Creditmemoshow"""
    # TODO: Add fields


class CreditmemoShowUpdate(BaseModel):
    """Update model for patching a Creditmemoshow"""
    # TODO: Add fields


class CreditmemoshowDb(BaseModel):
    """Internal DB representation for Creditmemoshow"""
    # TODO: Add fields
