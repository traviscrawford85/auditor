from pydantic import BaseModel


class TasktemplateShowIn(BaseModel):
    """Incoming model for creating a Tasktemplateshow"""
    # TODO: Add fields


class TasktemplateshowOut(BaseModel):
    """Outgoing model for returning a Tasktemplateshow"""
    # TODO: Add fields


class TasktemplateShowUpdate(BaseModel):
    """Update model for patching a Tasktemplateshow"""
    # TODO: Add fields


class TasktemplateshowDb(BaseModel):
    """Internal DB representation for Tasktemplateshow"""
    # TODO: Add fields
