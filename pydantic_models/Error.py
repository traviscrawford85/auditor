from pydantic import BaseModel
from typing import Optional, List


class ErrorIn(BaseModel):
    """Incoming model for creating a Error"""
    # TODO: Add fields


class ErrorOut(BaseModel):
    """Outgoing model for returning a Error"""
    # TODO: Add fields


class ErrorUpdate(BaseModel):
    """Update model for patching a Error"""
    # TODO: Add fields


class ErrorDb(BaseModel):
    """Internal DB representation for Error"""
    # TODO: Add fields
