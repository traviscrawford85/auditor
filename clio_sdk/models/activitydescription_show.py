
from pydantic import BaseModel

from .activitydescription import ActivitydescriptionOut


class ActivitydescriptionShowIn(BaseModel):
    data: ActivitydescriptionIn

class ActivitydescriptionShowOut(BaseModel):
    data: ActivitydescriptionOut

class ActivitydescriptionShowUpdate(BaseModel):
    data: ActivitydescriptionUpdate

class ActivitydescriptionShowDb(BaseModel):
    data: ActivitydescriptionDb

