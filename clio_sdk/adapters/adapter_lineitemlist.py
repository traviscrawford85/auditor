# Adapter for lineitemlist
from clio_sdk.models.lineitemlist import LineitemlistIn, LineitemlistOut, LineitemlistUpdate, LineitemlistDb
from clio_client.models import line_item_list

def convert_sdk_to_lineitemlistout(src: line_item_list) -> LineitemlistOut:
    return LineitemlistOut(**src.dict())

def convert_lineitemlistin_to_sdk(src: LineitemlistIn) -> line_item_list:
    return line_item_list(**src.dict())
