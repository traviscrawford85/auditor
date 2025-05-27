from typing import Optional

from pydantic import BaseModel


class MattercustomrateBaseIn(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomrateBaseOut(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomrateBaseUpdate(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

class MattercustomrateBaseDb(BaseModel):
    type: Optional[str] = None
    on_invoice: Optional[str] = None

