from pydantic import BaseModel


class TaskListIn(BaseModel):
    """Incoming model for creating a Tasklist"""
    # TODO: Add fields


class TasklistOut(BaseModel):
    """Outgoing model for returning a Tasklist"""
    # TODO: Add fields


class TasklistUpdate(BaseModel):
    """Update model for patching a Tasklist"""
    # TODO: Add fields


class TasklistDb(BaseModel):
    """Internal DB representation for Tasklist"""
    # TODO: Add fields
