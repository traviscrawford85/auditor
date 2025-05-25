from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukcivilcontrolledrateListIn(BaseModel):
    data: List[Any]

class LaukcivilcontrolledrateListOut(BaseModel):
    data: List[Any]

class LaukcivilcontrolledrateListUpdate(BaseModel):
    data: List[Any]

class LaukcivilcontrolledrateListDb(BaseModel):
    data: List[Any]

