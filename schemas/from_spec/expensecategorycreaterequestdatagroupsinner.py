from typing import Optional

from pydantic import BaseModel


class ExpensecategorycreaterequestdatagroupsinnerIn(BaseModel):
    id: Optional[str] = None
    _deleted: Optional[str] = None

class ExpensecategorycreaterequestdatagroupsinnerOut(BaseModel):
    id: Optional[str] = None
    _deleted: Optional[str] = None

class ExpensecategorycreaterequestdatagroupsinnerUpdate(BaseModel):
    id: Optional[str] = None
    _deleted: Optional[str] = None

class ExpensecategorycreaterequestdatagroupsinnerDb(BaseModel):
    id: Optional[str] = None
    _deleted: Optional[str] = None

