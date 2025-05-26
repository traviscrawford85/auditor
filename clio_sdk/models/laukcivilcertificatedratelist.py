from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukcivilcertificatedrateListIn(BaseModel):
    data: List[Laukcivilcertificatedrate]

class LaukcivilcertificatedrateListOut(BaseModel):
    data: List[Laukcivilcertificatedrate]

class LaukcivilcertificatedrateListUpdate(BaseModel):
    data: List[Laukcivilcertificatedrate]

class LaukcivilcertificatedrateListDb(BaseModel):
    data: List[Laukcivilcertificatedrate]

