from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalbillShowIn(BaseModel):
    data: Medicalbill

class MedicalbillShowOut(BaseModel):
    data: Medicalbill

class MedicalbillShowUpdate(BaseModel):
    data: Medicalbill

class MedicalbillShowDb(BaseModel):
    data: Medicalbill

