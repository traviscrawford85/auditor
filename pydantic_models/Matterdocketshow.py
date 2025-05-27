from pydantic import BaseModel


class MatterdocketShowIn(BaseModel):
    """Incoming model for creating a Matterdocketshow"""
    # TODO: Add fields


class MatterdocketshowOut(BaseModel):
    """Outgoing model for returning a Matterdocketshow"""
    # TODO: Add fields


class MatterdocketShowUpdate(BaseModel):
    """Update model for patching a Matterdocketshow"""
    # TODO: Add fields


class MatterdocketshowDb(BaseModel):
    """Internal DB representation for Matterdocketshow"""
    # TODO: Add fields
