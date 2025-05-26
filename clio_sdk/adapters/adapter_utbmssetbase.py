# Adapter for utbmssetbase
from clio_sdk.models.utbmssetbase import UtbmssetBaseIn, UtbmssetbaseOut, UtbmssetbaseUpdate, UtbmssetbaseDb
from clio_client.models.utbms_set import UtbmsSet

def convert_sdk_to_utbmssetbaseout(src: UtbmsSet) -> UtbmssetbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return UtbmssetbaseOut(**src.model_dump())

def convert_utbmssetbasein_to_sdk(src: UtbmssetBaseIn) -> UtbmsSet:
    """Converts a clio_sdk model to clio_client model."""
    return UtbmsSet(**src.model_dump())
