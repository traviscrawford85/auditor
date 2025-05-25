from pydantic import BaseModel
from typing import Optional, List


class EventmetricsIn(BaseModel):
    """Incoming model for creating a Eventmetrics"""
    # TODO: Add fields


class EventmetricsOut(BaseModel):
    """Outgoing model for returning a Eventmetrics"""
    # TODO: Add fields


class EventmetricsUpdate(BaseModel):
    """Update model for patching a Eventmetrics"""
    # TODO: Add fields


class EventmetricsDb(BaseModel):
    """Internal DB representation for Eventmetrics"""
    # TODO: Add fields
