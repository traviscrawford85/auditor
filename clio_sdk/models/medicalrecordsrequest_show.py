
from pydantic import BaseModel

from .medicalrecordsrequest import MedicalrecordsrequestOut


class MedicalrecordsrequestShowIn(BaseModel):
    data: MedicalrecordsrequestIn

class MedicalrecordsrequestShowOut(BaseModel):
    data: MedicalrecordsrequestOut

class MedicalrecordsrequestShowUpdate(BaseModel):
    data: MedicalrecordsrequestUpdate

class MedicalrecordsrequestShowDb(BaseModel):
    data: MedicalrecordsrequestDb

