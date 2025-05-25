from pydantic import BaseModel
from typing import Optional, List


class TasktemplateIn(BaseModel):
    """Incoming model for creating a Tasktemplate"""
    # TODO: Add fields


class TasktemplateOut(BaseModel):
    """Outgoing model for returning a Tasktemplate"""
    # TODO: Add fields


class TasktemplateUpdate(BaseModel):
    """Update model for patching a Tasktemplate"""
    # TODO: Add fields


class TasktemplateDb(BaseModel):
    """Internal DB representation for Tasktemplate"""
    # TODO: Add fields
