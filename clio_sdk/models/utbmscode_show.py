
from pydantic import BaseModel

from .utbmscode import UtbmscodeOut


class UtbmscodeShowIn(BaseModel):
    data: UtbmscodeIn

class UtbmscodeShowOut(BaseModel):
    data: UtbmscodeOut

class UtbmscodeShowUpdate(BaseModel):
    data: UtbmscodeUpdate

class UtbmscodeShowDb(BaseModel):
    data: UtbmscodeDb

