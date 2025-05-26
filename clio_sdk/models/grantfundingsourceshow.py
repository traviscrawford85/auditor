from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantfundingsourceShowIn(BaseModel):
    data: Grantfundingsource

class GrantfundingsourceShowOut(BaseModel):
    data: Grantfundingsource

class GrantfundingsourceShowUpdate(BaseModel):
    data: Grantfundingsource

class GrantfundingsourceShowDb(BaseModel):
    data: Grantfundingsource

