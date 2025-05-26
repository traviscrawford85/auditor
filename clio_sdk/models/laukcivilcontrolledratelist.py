from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukcivilcontrolledrateListIn(BaseModel):
    data: List[Laukcivilcontrolledrate]

class LaukcivilcontrolledrateListOut(BaseModel):
    data: List[Laukcivilcontrolledrate]

class LaukcivilcontrolledrateListUpdate(BaseModel):
    data: List[Laukcivilcontrolledrate]

class LaukcivilcontrolledrateListDb(BaseModel):
    data: List[Laukcivilcontrolledrate]

