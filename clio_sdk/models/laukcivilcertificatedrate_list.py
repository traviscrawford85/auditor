from typing import List

from pydantic import BaseModel

from .laukcivilcertificatedrate import LaukcivilcertificatedrateOut


class LaukcivilcertificatedrateListIn(BaseModel):
    data: List[LaukcivilcertificatedrateIn]

class LaukcivilcertificatedrateListOut(BaseModel):
    data: List[LaukcivilcertificatedrateOut]

class LaukcivilcertificatedrateListUpdate(BaseModel):
    data: List[LaukcivilcertificatedrateUpdate]

class LaukcivilcertificatedrateListDb(BaseModel):
    data: List[LaukcivilcertificatedrateDb]

