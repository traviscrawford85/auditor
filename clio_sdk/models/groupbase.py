from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GroupBaseIn(BaseModel):
    client_connect_user: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None

class GroupBaseOut(BaseModel):
    client_connect_user: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None

class GroupBaseUpdate(BaseModel):
    client_connect_user: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None

class GroupBaseDb(BaseModel):
    client_connect_user: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[datetime] = None

