from pydantic import BaseModel
from typing import Optional, List


class MatterdocketListIn(BaseModel):
    """Incoming model for creating a Matterdocketlist"""
    # TODO: Add fields


class MatterdocketlistOut(BaseModel):
    """Outgoing model for returning a Matterdocketlist"""
    # TODO: Add fields


class MatterdocketlistUpdate(BaseModel):
    """Update model for patching a Matterdocketlist"""
    # TODO: Add fields


class MatterdocketlistDb(BaseModel):
    """Internal DB representation for Matterdocketlist"""
    # TODO: Add fields
