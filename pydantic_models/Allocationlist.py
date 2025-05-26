from pydantic import BaseModel
from typing import Optional, List


class AllocationListIn(BaseModel):
    """Incoming model for creating a Allocationlist"""
    # TODO: Add fields


class AllocationlistOut(BaseModel):
    """Outgoing model for returning a Allocationlist"""
    # TODO: Add fields


class AllocationlistUpdate(BaseModel):
    """Update model for patching a Allocationlist"""
    # TODO: Add fields


class AllocationlistDb(BaseModel):
    """Internal DB representation for Allocationlist"""
    # TODO: Add fields
