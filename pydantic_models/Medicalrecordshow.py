from pydantic import BaseModel
from typing import Optional, List


class MedicalrecordShowIn(BaseModel):
    """Incoming model for creating a Medicalrecordshow"""
    # TODO: Add fields


class MedicalrecordshowOut(BaseModel):
    """Outgoing model for returning a Medicalrecordshow"""
    # TODO: Add fields


class MedicalrecordShowUpdate(BaseModel):
    """Update model for patching a Medicalrecordshow"""
    # TODO: Add fields


class MedicalrecordshowDb(BaseModel):
    """Internal DB representation for Medicalrecordshow"""
    # TODO: Add fields
