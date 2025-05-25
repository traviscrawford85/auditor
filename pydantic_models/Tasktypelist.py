from pydantic import BaseModel
from typing import Optional, List


class TasktypelistIn(BaseModel):
    """Incoming model for creating a Tasktypelist"""
    # TODO: Add fields


class TasktypelistOut(BaseModel):
    """Outgoing model for returning a Tasktypelist"""
    # TODO: Add fields


class TasktypelistUpdate(BaseModel):
    """Update model for patching a Tasktypelist"""
    # TODO: Add fields


class TasktypelistDb(BaseModel):
    """Internal DB representation for Tasktypelist"""
    # TODO: Add fields
