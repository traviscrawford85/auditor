from pydantic import BaseModel


class TypeIn(BaseModel):
    """Incoming model for creating a Type"""
    # TODO: Add fields


class TypeOut(BaseModel):
    """Outgoing model for returning a Type"""
    # TODO: Add fields


class TypeUpdate(BaseModel):
    """Update model for patching a Type"""
    # TODO: Add fields


class TypeDb(BaseModel):
    """Internal DB representation for Type"""
    # TODO: Add fields
