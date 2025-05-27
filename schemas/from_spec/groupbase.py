from typing import Optional

from pydantic import BaseModel


class GroupBaseIn(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class GroupBaseOut(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class GroupBaseUpdate(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

class GroupBaseDb(BaseModel):
    client_connect_user: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

