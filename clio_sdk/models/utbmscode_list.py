from typing import List

from pydantic import BaseModel

from .utbmscode import UtbmscodeOut


class UtbmscodeListIn(BaseModel):
    data: List[UtbmscodeIn]

class UtbmscodeListOut(BaseModel):
    data: List[UtbmscodeOut]

class UtbmscodeListUpdate(BaseModel):
    data: List[UtbmscodeUpdate]

class UtbmscodeListDb(BaseModel):
    data: List[UtbmscodeDb]

