from pydantic import BaseModel


class LogentryListIn(BaseModel):
    """Incoming model for creating a Logentrylist"""
    # TODO: Add fields


class LogentrylistOut(BaseModel):
    """Outgoing model for returning a Logentrylist"""
    # TODO: Add fields


class LogentrylistUpdate(BaseModel):
    """Update model for patching a Logentrylist"""
    # TODO: Add fields


class LogentrylistDb(BaseModel):
    """Internal DB representation for Logentrylist"""
    # TODO: Add fields
