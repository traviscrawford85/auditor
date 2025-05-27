from typing import List

from pydantic import BaseModel

from .activitydescription import ActivitydescriptionOut


class ActivitydescriptionListIn(BaseModel):
    data: List[ActivitydescriptionIn]

class ActivitydescriptionListOut(BaseModel):
    data: List[ActivitydescriptionOut]

class ActivitydescriptionListUpdate(BaseModel):
    data: List[ActivitydescriptionUpdate]

class ActivitydescriptionListDb(BaseModel):
    data: List[ActivitydescriptionDb]

