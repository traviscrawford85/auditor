from typing import List

from pydantic import BaseModel

from .laukcivilcontrolledrate import LaukcivilcontrolledrateOut


class LaukcivilcontrolledrateListIn(BaseModel):
    data: List[LaukcivilcontrolledrateIn]

class LaukcivilcontrolledrateListOut(BaseModel):
    data: List[LaukcivilcontrolledrateOut]

class LaukcivilcontrolledrateListUpdate(BaseModel):
    data: List[LaukcivilcontrolledrateUpdate]

class LaukcivilcontrolledrateListDb(BaseModel):
    data: List[LaukcivilcontrolledrateDb]

