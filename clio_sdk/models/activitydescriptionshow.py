from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitydescriptionShowIn(BaseModel):
    data: Activitydescription

class ActivitydescriptionShowOut(BaseModel):
    data: Activitydescription

class ActivitydescriptionShowUpdate(BaseModel):
    data: Activitydescription

class ActivitydescriptionShowDb(BaseModel):
    data: Activitydescription

