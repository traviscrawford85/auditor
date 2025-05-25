from pydantic import BaseModel
from typing import Optional, List


class RelationshipIn(BaseModel):
    """Incoming model for creating a Relationship"""
    # TODO: Add fields


class RelationshipOut(BaseModel):
    """Outgoing model for returning a Relationship"""
    # TODO: Add fields


class RelationshipUpdate(BaseModel):
    """Update model for patching a Relationship"""
    # TODO: Add fields


class RelationshipDb(BaseModel):
    """Internal DB representation for Relationship"""
    # TODO: Add fields
