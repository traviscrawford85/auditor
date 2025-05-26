from pydantic import BaseModel
from typing import Optional, List


class EventmetricsShowIn(BaseModel):
    """Incoming model for creating a Eventmetricsshow"""
    # TODO: Add fields


class EventmetricsshowOut(BaseModel):
    """Outgoing model for returning a Eventmetricsshow"""
    # TODO: Add fields


class EventmetricsShowUpdate(BaseModel):
    """Update model for patching a Eventmetricsshow"""
    # TODO: Add fields


class EventmetricsshowDb(BaseModel):
    """Internal DB representation for Eventmetricsshow"""
    # TODO: Add fields
