from typing import List

from pydantic import BaseModel

from .expensecategory import ExpensecategoryOut


class ExpensecategoryListIn(BaseModel):
    data: List[ExpensecategoryIn]

class ExpensecategoryListOut(BaseModel):
    data: List[ExpensecategoryOut]

class ExpensecategoryListUpdate(BaseModel):
    data: List[ExpensecategoryUpdate]

class ExpensecategoryListDb(BaseModel):
    data: List[ExpensecategoryDb]

