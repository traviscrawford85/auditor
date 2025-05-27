from typing import Optional

from pydantic import BaseModel


class MatterbalanceBaseIn(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None

class MatterbalanceBaseOut(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None

class MatterbalanceBaseUpdate(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None

class MatterbalanceBaseDb(BaseModel):
    id: Optional[int] = None
    amount: Optional[float] = None

