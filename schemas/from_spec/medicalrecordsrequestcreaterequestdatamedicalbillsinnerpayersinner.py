from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordsrequestcreaterequestdatamedicalbillsinnerpayersinnerIn(BaseModel):
    amount: str
    holder_id: int
    mark_as_lien: bool

class MedicalrecordsrequestcreaterequestdatamedicalbillsinnerpayersinnerOut(BaseModel):
    amount: str
    holder_id: int
    mark_as_lien: bool

class MedicalrecordsrequestcreaterequestdatamedicalbillsinnerpayersinnerUpdate(BaseModel):
    amount: str
    holder_id: int
    mark_as_lien: bool

class MedicalrecordsrequestcreaterequestdatamedicalbillsinnerpayersinnerDb(BaseModel):
    amount: str
    holder_id: int
    mark_as_lien: bool

