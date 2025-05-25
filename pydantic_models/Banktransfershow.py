from pydantic import BaseModel
from typing import Optional, List


class BanktransfershowIn(BaseModel):
    """Incoming model for creating a Banktransfershow"""
    # TODO: Add fields


class BanktransfershowOut(BaseModel):
    """Outgoing model for returning a Banktransfershow"""
    # TODO: Add fields


class BanktransfershowUpdate(BaseModel):
    """Update model for patching a Banktransfershow"""
    # TODO: Add fields


class BanktransfershowDb(BaseModel):
    """Internal DB representation for Banktransfershow"""
    # TODO: Add fields
