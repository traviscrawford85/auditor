from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillthemeShowIn(BaseModel):
    data: Any

class BillthemeShowOut(BaseModel):
    data: Any

class BillthemeShowUpdate(BaseModel):
    data: Any

class BillthemeShowDb(BaseModel):
    data: Any

