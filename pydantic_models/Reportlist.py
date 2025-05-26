from pydantic import BaseModel
from typing import Optional, List


class ReportListIn(BaseModel):
    """Incoming model for creating a Reportlist"""
    # TODO: Add fields


class ReportlistOut(BaseModel):
    """Outgoing model for returning a Reportlist"""
    # TODO: Add fields


class ReportlistUpdate(BaseModel):
    """Update model for patching a Reportlist"""
    # TODO: Add fields


class ReportlistDb(BaseModel):
    """Internal DB representation for Reportlist"""
    # TODO: Add fields
