from pydantic import BaseModel


class BanktransferIn(BaseModel):
    """Incoming model for creating a Banktransfer"""
    # TODO: Add fields


class BanktransferOut(BaseModel):
    """Outgoing model for returning a Banktransfer"""
    # TODO: Add fields


class BanktransferUpdate(BaseModel):
    """Update model for patching a Banktransfer"""
    # TODO: Add fields


class BanktransferDb(BaseModel):
    """Internal DB representation for Banktransfer"""
    # TODO: Add fields
