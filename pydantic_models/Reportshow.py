from pydantic import BaseModel


class ReportShowIn(BaseModel):
    """Incoming model for creating a Reportshow"""
    # TODO: Add fields


class ReportshowOut(BaseModel):
    """Outgoing model for returning a Reportshow"""
    # TODO: Add fields


class ReportShowUpdate(BaseModel):
    """Update model for patching a Reportshow"""
    # TODO: Add fields


class ReportshowDb(BaseModel):
    """Internal DB representation for Reportshow"""
    # TODO: Add fields
