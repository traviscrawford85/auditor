from pydantic import BaseModel


class ErrordetailIn(BaseModel):
    type: str
    message: str

class ErrordetailOut(BaseModel):
    type: str
    message: str

class ErrordetailUpdate(BaseModel):
    type: str
    message: str

class ErrordetailDb(BaseModel):
    type: str
    message: str

