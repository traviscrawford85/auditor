from typing import Optional

from pydantic import BaseModel


class LineitemBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[float] = None
    taxable: Optional[bool] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[bool] = None
    total: Optional[float] = None
    tax: Optional[float] = None
    secondary_tax: Optional[float] = None
    sub_total: Optional[float] = None
    quantity: Optional[float] = None
    group_ordering: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LineitemBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[float] = None
    taxable: Optional[bool] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[bool] = None
    total: Optional[float] = None
    tax: Optional[float] = None
    secondary_tax: Optional[float] = None
    sub_total: Optional[float] = None
    quantity: Optional[float] = None
    group_ordering: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LineitemBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[float] = None
    taxable: Optional[bool] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[bool] = None
    total: Optional[float] = None
    tax: Optional[float] = None
    secondary_tax: Optional[float] = None
    sub_total: Optional[float] = None
    quantity: Optional[float] = None
    group_ordering: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LineitemBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[float] = None
    taxable: Optional[bool] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[bool] = None
    total: Optional[float] = None
    tax: Optional[float] = None
    secondary_tax: Optional[float] = None
    sub_total: Optional[float] = None
    quantity: Optional[float] = None
    group_ordering: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

