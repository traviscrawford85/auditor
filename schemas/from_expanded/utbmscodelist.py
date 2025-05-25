from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmscodeListIn(BaseModel):
    data: List[Any]

class UtbmscodeListOut(BaseModel):
    data: List[Any]

class UtbmscodeListUpdate(BaseModel):
    data: List[Any]

class UtbmscodeListDb(BaseModel):
    data: List[Any]

