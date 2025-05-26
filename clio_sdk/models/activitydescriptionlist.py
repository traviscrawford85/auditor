from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitydescriptionListIn(BaseModel):
    data: List[Activitydescription]

class ActivitydescriptionListOut(BaseModel):
    data: List[Activitydescription]

class ActivitydescriptionListUpdate(BaseModel):
    data: List[Activitydescription]

class ActivitydescriptionListDb(BaseModel):
    data: List[Activitydescription]

