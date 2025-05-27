from typing import List

from pydantic import BaseModel

from .bankaccount import BankaccountOut


class BankaccountListIn(BaseModel):
    data: List[BankaccountIn]

class BankaccountListOut(BaseModel):
    data: List[BankaccountOut]

class BankaccountListUpdate(BaseModel):
    data: List[BankaccountUpdate]

class BankaccountListDb(BaseModel):
    data: List[BankaccountDb]

