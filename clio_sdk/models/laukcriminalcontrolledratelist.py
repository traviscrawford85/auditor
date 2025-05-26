from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukcriminalcontrolledrateListIn(BaseModel):
    data: List[Laukcriminalcontrolledrate]

class LaukcriminalcontrolledrateListOut(BaseModel):
    data: List[Laukcriminalcontrolledrate]

class LaukcriminalcontrolledrateListUpdate(BaseModel):
    data: List[Laukcriminalcontrolledrate]

class LaukcriminalcontrolledrateListDb(BaseModel):
    data: List[Laukcriminalcontrolledrate]

