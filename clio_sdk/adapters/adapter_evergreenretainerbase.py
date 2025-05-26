# Adapter for evergreenretainerbase
from clio_sdk.models.evergreenretainerbase import EvergreenretainerBaseIn, EvergreenretainerbaseOut, EvergreenretainerbaseUpdate, EvergreenretainerbaseDb
from clio_client.models.evergreen_retainer_base import EvergreenRetainerBase

def convert_sdk_to_evergreenretainerbaseout(src: EvergreenRetainerBase) -> EvergreenretainerbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return EvergreenretainerbaseOut(**src.model_dump())

def convert_evergreenretainerbasein_to_sdk(src: EvergreenretainerBaseIn) -> EvergreenRetainerBase:
    """Converts a clio_sdk model to clio_client model."""
    return EvergreenRetainerBase(**src.model_dump())
