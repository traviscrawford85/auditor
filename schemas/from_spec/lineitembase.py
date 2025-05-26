from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemBaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[str] = None
    taxable: Optional[str] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[str] = None
    total: Optional[str] = None
    tax: Optional[str] = None
    secondary_tax: Optional[str] = None
    sub_total: Optional[str] = None
    quantity: Optional[str] = None
    group_ordering: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LineitemBaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[str] = None
    taxable: Optional[str] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[str] = None
    total: Optional[str] = None
    tax: Optional[str] = None
    secondary_tax: Optional[str] = None
    sub_total: Optional[str] = None
    quantity: Optional[str] = None
    group_ordering: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LineitemBaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[str] = None
    taxable: Optional[str] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[str] = None
    total: Optional[str] = None
    tax: Optional[str] = None
    secondary_tax: Optional[str] = None
    sub_total: Optional[str] = None
    quantity: Optional[str] = None
    group_ordering: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class LineitemBaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[str] = None
    taxable: Optional[str] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[str] = None
    total: Optional[str] = None
    tax: Optional[str] = None
    secondary_tax: Optional[str] = None
    sub_total: Optional[str] = None
    quantity: Optional[str] = None
    group_ordering: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

