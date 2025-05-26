from pydantic import BaseModel
from typing import Optional, List


class RelationshipShowIn(BaseModel):
    """Incoming model for creating a Relationshipshow"""
    # TODO: Add fields


class RelationshipshowOut(BaseModel):
    """Outgoing model for returning a Relationshipshow"""
    # TODO: Add fields


class RelationshipShowUpdate(BaseModel):
    """Update model for patching a Relationshipshow"""
    # TODO: Add fields


class RelationshipshowDb(BaseModel):
    """Internal DB representation for Relationshipshow"""
    # TODO: Add fields
