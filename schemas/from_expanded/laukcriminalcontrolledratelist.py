from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukcriminalcontrolledrateListIn(BaseModel):
    data: List[Any]

class LaukcriminalcontrolledrateListOut(BaseModel):
    data: List[Any]

class LaukcriminalcontrolledrateListUpdate(BaseModel):
    data: List[Any]

class LaukcriminalcontrolledrateListDb(BaseModel):
    data: List[Any]

