from pydantic import BaseModel


class CalendarListIn(BaseModel):
    """Incoming model for creating a Calendarlist"""
    # TODO: Add fields


class CalendarlistOut(BaseModel):
    """Outgoing model for returning a Calendarlist"""
    # TODO: Add fields


class CalendarlistUpdate(BaseModel):
    """Update model for patching a Calendarlist"""
    # TODO: Add fields


class CalendarlistDb(BaseModel):
    """Internal DB representation for Calendarlist"""
    # TODO: Add fields
