# Adapter for lineitemshow
from clio_sdk.models.lineitemshow import LineitemshowIn, LineitemshowOut, LineitemshowUpdate, LineitemshowDb
from clio_client.models.line_item_show import LineItemShow

def convert_sdk_to_lineitemshowout(src: LineItemShow) -> LineitemshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return LineitemshowOut(**src.model_dump())

def convert_lineitemshowin_to_sdk(src: LineitemshowIn) -> LineItemShow:
    """Converts a clio_sdk model to clio_client model."""
    return LineItemShow(**src.model_dump())
