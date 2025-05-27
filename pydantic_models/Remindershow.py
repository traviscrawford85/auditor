from pydantic import BaseModel


class ReminderShowIn(BaseModel):
    """Incoming model for creating a Remindershow"""
    # TODO: Add fields


class RemindershowOut(BaseModel):
    """Outgoing model for returning a Remindershow"""
    # TODO: Add fields


class ReminderShowUpdate(BaseModel):
    """Update model for patching a Remindershow"""
    # TODO: Add fields


class RemindershowDb(BaseModel):
    """Internal DB representation for Remindershow"""
    # TODO: Add fields
