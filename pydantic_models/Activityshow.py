from pydantic import BaseModel


class ActivityShowIn(BaseModel):
    """Incoming model for creating a Activityshow"""
    # TODO: Add fields


class ActivityshowOut(BaseModel):
    """Outgoing model for returning a Activityshow"""
    # TODO: Add fields


class ActivityShowUpdate(BaseModel):
    """Update model for patching a Activityshow"""
    # TODO: Add fields


class ActivityshowDb(BaseModel):
    """Internal DB representation for Activityshow"""
    # TODO: Add fields
