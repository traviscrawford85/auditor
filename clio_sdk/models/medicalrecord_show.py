
from pydantic import BaseModel

from .medicalrecord import MedicalrecordOut


class MedicalrecordShowIn(BaseModel):
    data: MedicalrecordIn

class MedicalrecordShowOut(BaseModel):
    data: MedicalrecordOut

class MedicalrecordShowUpdate(BaseModel):
    data: MedicalrecordUpdate

class MedicalrecordShowDb(BaseModel):
    data: MedicalrecordDb

