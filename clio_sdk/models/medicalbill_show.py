
from pydantic import BaseModel

from .medicalbill import MedicalbillOut


class MedicalbillShowIn(BaseModel):
    data: MedicalbillIn

class MedicalbillShowOut(BaseModel):
    data: MedicalbillOut

class MedicalbillShowUpdate(BaseModel):
    data: MedicalbillUpdate

class MedicalbillShowDb(BaseModel):
    data: MedicalbillDb

