from pydantic import BaseModel


class CalendarShowIn(BaseModel):
    """Incoming model for creating a Calendarshow"""
    # TODO: Add fields


class CalendarshowOut(BaseModel):
    """Outgoing model for returning a Calendarshow"""
    # TODO: Add fields


class CalendarShowUpdate(BaseModel):
    """Update model for patching a Calendarshow"""
    # TODO: Add fields


class CalendarshowDb(BaseModel):
    """Internal DB representation for Calendarshow"""
    # TODO: Add fields
