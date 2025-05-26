from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillingsettingShowIn(BaseModel):
    data: Billingsetting

class BillingsettingShowOut(BaseModel):
    data: Billingsetting

class BillingsettingShowUpdate(BaseModel):
    data: Billingsetting

class BillingsettingShowDb(BaseModel):
    data: Billingsetting

