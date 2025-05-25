from pydantic import BaseModel
from typing import Optional, List


class ExpensecategoryIn(BaseModel):
    """Incoming model for creating a Expensecategory"""
    # TODO: Add fields


class ExpensecategoryOut(BaseModel):
    """Outgoing model for returning a Expensecategory"""
    # TODO: Add fields


class ExpensecategoryUpdate(BaseModel):
    """Update model for patching a Expensecategory"""
    # TODO: Add fields


class ExpensecategoryDb(BaseModel):
    """Internal DB representation for Expensecategory"""
    # TODO: Add fields
