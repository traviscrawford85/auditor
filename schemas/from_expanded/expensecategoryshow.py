from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ExpensecategoryShowIn(BaseModel):
    data: Any

class ExpensecategoryShowOut(BaseModel):
    data: Any

class ExpensecategoryShowUpdate(BaseModel):
    data: Any

class ExpensecategoryShowDb(BaseModel):
    data: Any

