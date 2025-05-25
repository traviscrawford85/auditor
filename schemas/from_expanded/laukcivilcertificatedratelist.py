from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukcivilcertificatedrateListIn(BaseModel):
    data: List[Any]

class LaukcivilcertificatedrateListOut(BaseModel):
    data: List[Any]

class LaukcivilcertificatedrateListUpdate(BaseModel):
    data: List[Any]

class LaukcivilcertificatedrateListDb(BaseModel):
    data: List[Any]

