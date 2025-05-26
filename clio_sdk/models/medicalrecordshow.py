from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordShowIn(BaseModel):
    data: Medicalrecord

class MedicalrecordShowOut(BaseModel):
    data: Medicalrecord

class MedicalrecordShowUpdate(BaseModel):
    data: Medicalrecord

class MedicalrecordShowDb(BaseModel):
    data: Medicalrecord

