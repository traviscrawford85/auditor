from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BillthemeShowIn(BaseModel):
    data: Billtheme

class BillthemeShowOut(BaseModel):
    data: Billtheme

class BillthemeShowUpdate(BaseModel):
    data: Billtheme

class BillthemeShowDb(BaseModel):
    data: Billtheme

