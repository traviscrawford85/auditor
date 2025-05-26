from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustrequestShowIn(BaseModel):
    data: Trustrequest

class TrustrequestShowOut(BaseModel):
    data: Trustrequest

class TrustrequestShowUpdate(BaseModel):
    data: Trustrequest

class TrustrequestShowDb(BaseModel):
    data: Trustrequest

