# Adapter for lineitemtotalsbase
from clio_sdk.models.lineitemtotalsbase import LineitemtotalsBaseIn, LineitemtotalsbaseOut, LineitemtotalsbaseUpdate, LineitemtotalsbaseDb
from clio_client.models.line_item_totals_base import LineItemTotalsBase

def convert_sdk_to_lineitemtotalsbaseout(src: LineItemTotalsBase) -> LineitemtotalsbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LineitemtotalsbaseOut(**src.model_dump())

def convert_lineitemtotalsbasein_to_sdk(src: LineitemtotalsBaseIn) -> LineItemTotalsBase:
    """Converts a clio_sdk model to clio_client model."""
    return LineItemTotalsBase(**src.model_dump())
