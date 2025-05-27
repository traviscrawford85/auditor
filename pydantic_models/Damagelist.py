from pydantic import BaseModel


class DamageListIn(BaseModel):
    """Incoming model for creating a Damagelist"""
    # TODO: Add fields


class DamagelistOut(BaseModel):
    """Outgoing model for returning a Damagelist"""
    # TODO: Add fields


class DamagelistUpdate(BaseModel):
    """Update model for patching a Damagelist"""
    # TODO: Add fields


class DamagelistDb(BaseModel):
    """Internal DB representation for Damagelist"""
    # TODO: Add fields
