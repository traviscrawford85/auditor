from pydantic import BaseModel


class ReminderListIn(BaseModel):
    """Incoming model for creating a Reminderlist"""
    # TODO: Add fields


class ReminderlistOut(BaseModel):
    """Outgoing model for returning a Reminderlist"""
    # TODO: Add fields


class ReminderlistUpdate(BaseModel):
    """Update model for patching a Reminderlist"""
    # TODO: Add fields


class ReminderlistDb(BaseModel):
    """Internal DB representation for Reminderlist"""
    # TODO: Add fields
