from typing import List

from pydantic import BaseModel

from .mattercontacts import MattercontactsOut


class MattercontactsListIn(BaseModel):
    data: List[MattercontactsIn]

class MattercontactsListOut(BaseModel):
    data: List[MattercontactsOut]

class MattercontactsListUpdate(BaseModel):
    data: List[MattercontactsUpdate]

class MattercontactsListDb(BaseModel):
    data: List[MattercontactsDb]

