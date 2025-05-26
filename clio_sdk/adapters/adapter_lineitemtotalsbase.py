# Adapter for lineitemtotalsbase
from clio_sdk.models.lineitemtotalsbase import LineitemtotalsbaseIn, LineitemtotalsbaseOut, LineitemtotalsbaseUpdate, LineitemtotalsbaseDb
from clio_client.models import line_item_totals_base

def convert_sdk_to_lineitemtotalsbaseout(src: line_item_totals_base) -> LineitemtotalsbaseOut:
    return LineitemtotalsbaseOut(**src.dict())

def convert_lineitemtotalsbasein_to_sdk(src: LineitemtotalsbaseIn) -> line_item_totals_base:
    return line_item_totals_base(**src.dict())
