
from pydantic import BaseModel

from .banktransfer import BanktransferOut


class BanktransferShowIn(BaseModel):
    data: BanktransferIn

class BanktransferShowOut(BaseModel):
    data: BanktransferOut

class BanktransferShowUpdate(BaseModel):
    data: BanktransferUpdate

class BanktransferShowDb(BaseModel):
    data: BanktransferDb

