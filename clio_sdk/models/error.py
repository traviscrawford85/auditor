from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ErrorIn(BaseModel):
    error: Errordetail

class ErrorOut(BaseModel):
    error: Errordetail

class ErrorUpdate(BaseModel):
    error: Errordetail

class ErrorDb(BaseModel):
    error: Errordetail

