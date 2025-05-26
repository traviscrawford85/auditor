from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UtbmscodeShowIn(BaseModel):
    data: Utbmscode

class UtbmscodeShowOut(BaseModel):
    data: Utbmscode

class UtbmscodeShowUpdate(BaseModel):
    data: Utbmscode

class UtbmscodeShowDb(BaseModel):
    data: Utbmscode

