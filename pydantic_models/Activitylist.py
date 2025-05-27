from pydantic import BaseModel


class ActivityListIn(BaseModel):
    """Incoming model for creating a Activitylist"""
    # TODO: Add fields


class ActivitylistOut(BaseModel):
    """Outgoing model for returning a Activitylist"""
    # TODO: Add fields


class ActivitylistUpdate(BaseModel):
    """Update model for patching a Activitylist"""
    # TODO: Add fields


class ActivitylistDb(BaseModel):
    """Internal DB representation for Activitylist"""
    # TODO: Add fields
