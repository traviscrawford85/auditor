# Adapter for lineitembase
from clio_sdk.models.lineitembase import LineitembaseIn, LineitembaseOut, LineitembaseUpdate, LineitembaseDb
from clio_client.models import line_item

def convert_sdk_to_lineitembaseout(src: line_item) -> LineitembaseOut:
    return LineitembaseOut(**src.dict())

def convert_lineitembasein_to_sdk(src: LineitembaseIn) -> line_item:
    return line_item(**src.dict())
