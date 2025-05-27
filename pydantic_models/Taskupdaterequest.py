from pydantic import BaseModel


class TaskupdaterequestIn(BaseModel):
    """Incoming model for creating a Taskupdaterequest"""
    # TODO: Add fields


class TaskupdaterequestOut(BaseModel):
    """Outgoing model for returning a Taskupdaterequest"""
    # TODO: Add fields


class TaskupdaterequestUpdate(BaseModel):
    """Update model for patching a Taskupdaterequest"""
    # TODO: Add fields


class TaskupdaterequestDb(BaseModel):
    """Internal DB representation for Taskupdaterequest"""
    # TODO: Add fields
