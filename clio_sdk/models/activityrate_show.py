
from pydantic import BaseModel

from .activityrate import ActivityrateOut


class ActivityrateShowIn(BaseModel):
    data: ActivityrateIn

class ActivityrateShowOut(BaseModel):
    data: ActivityrateOut

class ActivityrateShowUpdate(BaseModel):
    data: ActivityrateUpdate

class ActivityrateShowDb(BaseModel):
    data: ActivityrateDb

