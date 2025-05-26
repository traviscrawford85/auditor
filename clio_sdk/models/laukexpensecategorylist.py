from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LaukexpensecategoryListIn(BaseModel):
    data: List[Laukexpensecategory]

class LaukexpensecategoryListOut(BaseModel):
    data: List[Laukexpensecategory]

class LaukexpensecategoryListUpdate(BaseModel):
    data: List[Laukexpensecategory]

class LaukexpensecategoryListDb(BaseModel):
    data: List[Laukexpensecategory]

