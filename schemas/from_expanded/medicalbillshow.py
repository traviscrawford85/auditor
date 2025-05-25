from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalbillShowIn(BaseModel):
    data: Any

class MedicalbillShowOut(BaseModel):
    data: Any

class MedicalbillShowUpdate(BaseModel):
    data: Any

class MedicalbillShowDb(BaseModel):
    data: Any

