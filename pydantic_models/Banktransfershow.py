from pydantic import BaseModel


class BanktransferShowIn(BaseModel):
    """Incoming model for creating a Banktransfershow"""
    # TODO: Add fields


class BanktransfershowOut(BaseModel):
    """Outgoing model for returning a Banktransfershow"""
    # TODO: Add fields


class BanktransferShowUpdate(BaseModel):
    """Update model for patching a Banktransfershow"""
    # TODO: Add fields


class BanktransfershowDb(BaseModel):
    """Internal DB representation for Banktransfershow"""
    # TODO: Add fields
