from pydantic import BaseModel
from typing import Optional, List


class ReportscheduleIn(BaseModel):
    """Incoming model for creating a Reportschedule"""
    # TODO: Add fields


class ReportscheduleOut(BaseModel):
    """Outgoing model for returning a Reportschedule"""
    # TODO: Add fields


class ReportscheduleUpdate(BaseModel):
    """Update model for patching a Reportschedule"""
    # TODO: Add fields


class ReportscheduleDb(BaseModel):
    """Internal DB representation for Reportschedule"""
    # TODO: Add fields
