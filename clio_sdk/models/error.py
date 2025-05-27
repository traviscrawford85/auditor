
from pydantic import BaseModel

from .errordetail import ErrordetailOut


class ErrorIn(BaseModel):
    error: ErrordetailIn

class ErrorOut(BaseModel):
    error: ErrordetailOut

class ErrorUpdate(BaseModel):
    error: ErrordetailUpdate

class ErrorDb(BaseModel):
    error: ErrordetailDb

