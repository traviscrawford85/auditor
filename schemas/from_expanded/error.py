from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ErrorIn(BaseModel):
    error: Any

class ErrorOut(BaseModel):
    error: Any

class ErrorUpdate(BaseModel):
    error: Any

class ErrorDb(BaseModel):
    error: Any

