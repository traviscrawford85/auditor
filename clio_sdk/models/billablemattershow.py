from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillablematterShowIn(BaseModel):
    data: Billablematter

class BillablematterShowOut(BaseModel):
    data: Billablematter

class BillablematterShowUpdate(BaseModel):
    data: Billablematter

class BillablematterShowDb(BaseModel):
    data: Billablematter

