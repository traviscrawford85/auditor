# Adapter for utbmssetlist
from clio_sdk.models.utbmssetlist import UtbmssetlistIn, UtbmssetlistOut, UtbmssetlistUpdate, UtbmssetlistDb
from clio_client.models.utbms_set_list import UtbmsSetList

def convert_sdk_to_utbmssetlistout(src: UtbmsSetList) -> UtbmssetlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return UtbmssetlistOut(**src.model_dump())

def convert_utbmssetlistin_to_sdk(src: UtbmssetlistIn) -> UtbmsSetList:
    """Converts a clio_sdk model to clio_client model."""
    return UtbmsSetList(**src.model_dump())
