from pydantic import BaseModel
from typing import Optional, List


class MedicalrecordIn(BaseModel):
    """Incoming model for creating a Medicalrecord"""
    # TODO: Add fields


class MedicalrecordOut(BaseModel):
    """Outgoing model for returning a Medicalrecord"""
    # TODO: Add fields


class MedicalrecordUpdate(BaseModel):
    """Update model for patching a Medicalrecord"""
    # TODO: Add fields


class MedicalrecordDb(BaseModel):
    """Internal DB representation for Medicalrecord"""
    # TODO: Add fields
