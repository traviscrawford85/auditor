from typing import Optional

from pydantic import BaseModel


class DamageupdaterequestdataIn(BaseModel):
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None

class DamageupdaterequestdataOut(BaseModel):
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None

class DamageupdaterequestdataUpdate(BaseModel):
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None

class DamageupdaterequestdataDb(BaseModel):
    amount: Optional[str] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None

