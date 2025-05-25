from pydantic import BaseModel
from typing import Optional, List


class ReminderIn(BaseModel):
    """Incoming model for creating a Reminder"""
    # TODO: Add fields


class ReminderOut(BaseModel):
    """Outgoing model for returning a Reminder"""
    # TODO: Add fields


class ReminderUpdate(BaseModel):
    """Update model for patching a Reminder"""
    # TODO: Add fields


class ReminderDb(BaseModel):
    """Internal DB representation for Reminder"""
    # TODO: Add fields
