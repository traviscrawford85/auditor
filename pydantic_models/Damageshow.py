from pydantic import BaseModel


class DamageShowIn(BaseModel):
    """Incoming model for creating a Damageshow"""
    # TODO: Add fields


class DamageshowOut(BaseModel):
    """Outgoing model for returning a Damageshow"""
    # TODO: Add fields


class DamageShowUpdate(BaseModel):
    """Update model for patching a Damageshow"""
    # TODO: Add fields


class DamageshowDb(BaseModel):
    """Internal DB representation for Damageshow"""
    # TODO: Add fields
