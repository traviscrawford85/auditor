from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmscodeListIn(BaseModel):
    data: List[Utbmscode]

class UtbmscodeListOut(BaseModel):
    data: List[Utbmscode]

class UtbmscodeListUpdate(BaseModel):
    data: List[Utbmscode]

class UtbmscodeListDb(BaseModel):
    data: List[Utbmscode]

