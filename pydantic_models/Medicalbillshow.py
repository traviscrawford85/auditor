from pydantic import BaseModel


class MedicalbillShowIn(BaseModel):
    """Incoming model for creating a Medicalbillshow"""
    # TODO: Add fields


class MedicalbillshowOut(BaseModel):
    """Outgoing model for returning a Medicalbillshow"""
    # TODO: Add fields


class MedicalbillShowUpdate(BaseModel):
    """Update model for patching a Medicalbillshow"""
    # TODO: Add fields


class MedicalbillshowDb(BaseModel):
    """Internal DB representation for Medicalbillshow"""
    # TODO: Add fields
