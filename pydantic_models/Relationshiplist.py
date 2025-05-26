from pydantic import BaseModel
from typing import Optional, List


class RelationshipListIn(BaseModel):
    """Incoming model for creating a Relationshiplist"""
    # TODO: Add fields


class RelationshiplistOut(BaseModel):
    """Outgoing model for returning a Relationshiplist"""
    # TODO: Add fields


class RelationshiplistUpdate(BaseModel):
    """Update model for patching a Relationshiplist"""
    # TODO: Add fields


class RelationshiplistDb(BaseModel):
    """Internal DB representation for Relationshiplist"""
    # TODO: Add fields
