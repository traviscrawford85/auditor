from typing import List

from pydantic import BaseModel

from .laukcriminalcontrolledrate import LaukcriminalcontrolledrateOut


class LaukcriminalcontrolledrateListIn(BaseModel):
    data: List[LaukcriminalcontrolledrateIn]

class LaukcriminalcontrolledrateListOut(BaseModel):
    data: List[LaukcriminalcontrolledrateOut]

class LaukcriminalcontrolledrateListUpdate(BaseModel):
    data: List[LaukcriminalcontrolledrateUpdate]

class LaukcriminalcontrolledrateListDb(BaseModel):
    data: List[LaukcriminalcontrolledrateDb]

