from pydantic import BaseModel


class DamagecreaterequestdataIn(BaseModel):
    amount: str
    damage_type: str
    description: str
    matter_id: int

class DamagecreaterequestdataOut(BaseModel):
    amount: str
    damage_type: str
    description: str
    matter_id: int

class DamagecreaterequestdataUpdate(BaseModel):
    amount: str
    damage_type: str
    description: str
    matter_id: int

class DamagecreaterequestdataDb(BaseModel):
    amount: str
    damage_type: str
    description: str
    matter_id: int

