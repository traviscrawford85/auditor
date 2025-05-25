from pydantic import BaseModel
from typing import Optional, List


class CalendarIn(BaseModel):
    """Incoming model for creating a Calendar"""
    # TODO: Add fields


class CalendarOut(BaseModel):
    """Outgoing model for returning a Calendar"""
    # TODO: Add fields


class CalendarUpdate(BaseModel):
    """Update model for patching a Calendar"""
    # TODO: Add fields


class CalendarDb(BaseModel):
    """Internal DB representation for Calendar"""
    # TODO: Add fields
