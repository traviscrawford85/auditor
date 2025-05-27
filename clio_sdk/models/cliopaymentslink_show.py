
from pydantic import BaseModel

from .cliopaymentslink import CliopaymentslinkOut


class CliopaymentslinkShowIn(BaseModel):
    data: CliopaymentslinkIn

class CliopaymentslinkShowOut(BaseModel):
    data: CliopaymentslinkOut

class CliopaymentslinkShowUpdate(BaseModel):
    data: CliopaymentslinkUpdate

class CliopaymentslinkShowDb(BaseModel):
    data: CliopaymentslinkDb

