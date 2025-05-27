from pydantic import BaseModel


class ReportIn(BaseModel):
    """Incoming model for creating a Report"""
    # TODO: Add fields


class ReportOut(BaseModel):
    """Outgoing model for returning a Report"""
    # TODO: Add fields


class ReportUpdate(BaseModel):
    """Update model for patching a Report"""
    # TODO: Add fields


class ReportDb(BaseModel):
    """Internal DB representation for Report"""
    # TODO: Add fields
