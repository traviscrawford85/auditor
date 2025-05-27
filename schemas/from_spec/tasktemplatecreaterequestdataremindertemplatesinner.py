from pydantic import BaseModel


class TasktemplatecreaterequestdataremindertemplatesinnerIn(BaseModel):
    duration_value: int
    duration_unit: str
    notification_type: str

class TasktemplatecreaterequestdataremindertemplatesinnerOut(BaseModel):
    duration_value: int
    duration_unit: str
    notification_type: str

class TasktemplatecreaterequestdataremindertemplatesinnerUpdate(BaseModel):
    duration_value: int
    duration_unit: str
    notification_type: str

class TasktemplatecreaterequestdataremindertemplatesinnerDb(BaseModel):
    duration_value: int
    duration_unit: str
    notification_type: str

