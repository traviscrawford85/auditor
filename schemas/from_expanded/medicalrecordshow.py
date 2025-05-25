from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordShowIn(BaseModel):
    data: Any

class MedicalrecordShowOut(BaseModel):
    data: Any

class MedicalrecordShowUpdate(BaseModel):
    data: Any

class MedicalrecordShowDb(BaseModel):
    data: Any

