from pydantic import BaseModel


class MedicalbillIn(BaseModel):
    """Incoming model for creating a Medicalbill"""
    # TODO: Add fields


class MedicalbillOut(BaseModel):
    """Outgoing model for returning a Medicalbill"""
    # TODO: Add fields


class MedicalbillUpdate(BaseModel):
    """Update model for patching a Medicalbill"""
    # TODO: Add fields


class MedicalbillDb(BaseModel):
    """Internal DB representation for Medicalbill"""
    # TODO: Add fields
