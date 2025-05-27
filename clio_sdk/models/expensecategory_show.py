
from pydantic import BaseModel

from .expensecategory import ExpensecategoryOut


class ExpensecategoryShowIn(BaseModel):
    data: ExpensecategoryIn

class ExpensecategoryShowOut(BaseModel):
    data: ExpensecategoryOut

class ExpensecategoryShowUpdate(BaseModel):
    data: ExpensecategoryUpdate

class ExpensecategoryShowDb(BaseModel):
    data: ExpensecategoryDb

