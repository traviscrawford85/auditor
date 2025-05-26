# Adapter for lineitembase
from clio_sdk.models.lineitembase import LineitemBaseIn, LineitembaseOut, LineitembaseUpdate, LineitembaseDb
from clio_client.models.line_item import LineItem

def convert_sdk_to_lineitembaseout(src: LineItem) -> LineitembaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LineitembaseOut(**src.model_dump())

def convert_lineitembasein_to_sdk(src: LineitemBaseIn) -> LineItem:
    """Converts a clio_sdk model to clio_client model."""
    return LineItem(**src.model_dump())
