# Adapter for lineitemlist
from clio_sdk.models.lineitemlist import LineitemlistIn, LineitemlistOut, LineitemlistUpdate, LineitemlistDb
from clio_client.models.line_item_list import LineItemList

def convert_sdk_to_lineitemlistout(src: LineItemList) -> LineitemlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return LineitemlistOut(**src.model_dump())

def convert_lineitemlistin_to_sdk(src: LineitemlistIn) -> LineItemList:
    """Converts a clio_sdk model to clio_client model."""
    return LineItemList(**src.model_dump())
