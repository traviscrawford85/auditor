
from pydantic import BaseModel

from .trustrequest import TrustrequestOut


class TrustrequestShowIn(BaseModel):
    data: TrustrequestIn

class TrustrequestShowOut(BaseModel):
    data: TrustrequestOut

class TrustrequestShowUpdate(BaseModel):
    data: TrustrequestUpdate

class TrustrequestShowDb(BaseModel):
    data: TrustrequestDb

