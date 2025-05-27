
from pydantic import BaseModel


class StatuteoflimitationscomputerequestIn(BaseModel):
    date_of_incident: str

class StatuteoflimitationscomputerequestOut(BaseModel):
    date_of_incident: str

class StatuteoflimitationscomputerequestUpdate(BaseModel):
    date_of_incident: str

class StatuteoflimitationscomputerequestDb(BaseModel):
    date_of_incident: str

