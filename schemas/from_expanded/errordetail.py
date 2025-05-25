from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ErrordetailIn(BaseModel):
    type: str
    message: str

class ErrordetailOut(BaseModel):
    type: str
    message: str

class ErrordetailUpdate(BaseModel):
    type: str
    message: str

class ErrordetailDb(BaseModel):
    type: str
    message: str

