from pydantic import BaseModel


class AllocationIn(BaseModel):
    """Incoming model for creating a Allocation"""
    # TODO: Add fields


class AllocationOut(BaseModel):
    """Outgoing model for returning a Allocation"""
    # TODO: Add fields


class AllocationUpdate(BaseModel):
    """Update model for patching a Allocation"""
    # TODO: Add fields


class AllocationDb(BaseModel):
    """Internal DB representation for Allocation"""
    # TODO: Add fields
