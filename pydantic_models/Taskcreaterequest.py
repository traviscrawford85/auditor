from pydantic import BaseModel
from typing import Optional, List


class TaskcreaterequestIn(BaseModel):
    """Incoming model for creating a Taskcreaterequest"""
    # TODO: Add fields


class TaskcreaterequestOut(BaseModel):
    """Outgoing model for returning a Taskcreaterequest"""
    # TODO: Add fields


class TaskcreaterequestUpdate(BaseModel):
    """Update model for patching a Taskcreaterequest"""
    # TODO: Add fields


class TaskcreaterequestDb(BaseModel):
    """Internal DB representation for Taskcreaterequest"""
    # TODO: Add fields
