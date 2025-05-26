from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExpensecategoryListIn(BaseModel):
    data: List[Expensecategory]

class ExpensecategoryListOut(BaseModel):
    data: List[Expensecategory]

class ExpensecategoryListUpdate(BaseModel):
    data: List[Expensecategory]

class ExpensecategoryListDb(BaseModel):
    data: List[Expensecategory]

