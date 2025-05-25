from pydantic import BaseModel
from typing import Optional, List


class CalendarentryIn(BaseModel):
    """Incoming model for creating a Calendarentry"""
    # TODO: Add fields


class CalendarentryOut(BaseModel):
    """Outgoing model for returning a Calendarentry"""
    # TODO: Add fields


class CalendarentryUpdate(BaseModel):
    """Update model for patching a Calendarentry"""
    # TODO: Add fields


class CalendarentryDb(BaseModel):
    """Internal DB representation for Calendarentry"""
    # TODO: Add fields
