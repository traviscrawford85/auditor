
from pydantic import BaseModel

from .bankaccount import BankaccountOut


class BankaccountShowIn(BaseModel):
    data: BankaccountIn

class BankaccountShowOut(BaseModel):
    data: BankaccountOut

class BankaccountShowUpdate(BaseModel):
    data: BankaccountUpdate

class BankaccountShowDb(BaseModel):
    data: BankaccountDb

