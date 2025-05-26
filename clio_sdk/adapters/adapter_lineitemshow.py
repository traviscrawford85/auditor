# Adapter for lineitemshow
from clio_sdk.models.lineitemshow import LineitemshowIn, LineitemshowOut, LineitemshowUpdate, LineitemshowDb
from clio_client.models import line_item_show

def convert_sdk_to_lineitemshowout(src: line_item_show) -> LineitemshowOut:
    return LineitemshowOut(**src.dict())

def convert_lineitemshowin_to_sdk(src: LineitemshowIn) -> line_item_show:
    return line_item_show(**src.dict())
