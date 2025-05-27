from pydantic import BaseModel


class LogentryIn(BaseModel):
    """Incoming model for creating a Logentry"""
    # TODO: Add fields


class LogentryOut(BaseModel):
    """Outgoing model for returning a Logentry"""
    # TODO: Add fields


class LogentryUpdate(BaseModel):
    """Update model for patching a Logentry"""
    # TODO: Add fields


class LogentryDb(BaseModel):
    """Internal DB representation for Logentry"""
    # TODO: Add fields
