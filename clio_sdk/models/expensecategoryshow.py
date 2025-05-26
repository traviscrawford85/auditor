from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExpensecategoryShowIn(BaseModel):
    data: Expensecategory

class ExpensecategoryShowOut(BaseModel):
    data: Expensecategory

class ExpensecategoryShowUpdate(BaseModel):
    data: Expensecategory

class ExpensecategoryShowDb(BaseModel):
    data: Expensecategory

