from pydantic import BaseModel


class AllocationShowIn(BaseModel):
    """Incoming model for creating a Allocationshow"""
    # TODO: Add fields


class AllocationshowOut(BaseModel):
    """Outgoing model for returning a Allocationshow"""
    # TODO: Add fields


class AllocationShowUpdate(BaseModel):
    """Update model for patching a Allocationshow"""
    # TODO: Add fields


class AllocationshowDb(BaseModel):
    """Internal DB representation for Allocationshow"""
    # TODO: Add fields
