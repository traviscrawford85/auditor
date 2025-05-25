from pydantic import BaseModel
from typing import Optional, List


class ErrordetailIn(BaseModel):
    """Incoming model for creating a Errordetail"""
    # TODO: Add fields


class ErrordetailOut(BaseModel):
    """Outgoing model for returning a Errordetail"""
    # TODO: Add fields


class ErrordetailUpdate(BaseModel):
    """Update model for patching a Errordetail"""
    # TODO: Add fields


class ErrordetailDb(BaseModel):
    """Internal DB representation for Errordetail"""
    # TODO: Add fields
