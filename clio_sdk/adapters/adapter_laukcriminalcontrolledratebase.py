# Adapter for laukcriminalcontrolledratebase
from clio_sdk.models.laukcriminalcontrolledratebase import LaukcriminalcontrolledrateBaseIn, LaukcriminalcontrolledratebaseOut, LaukcriminalcontrolledratebaseUpdate, LaukcriminalcontrolledratebaseDb
from clio_client.models.lauk_criminal_controlled_rate import LaukCriminalControlledRate

def convert_sdk_to_laukcriminalcontrolledratebaseout(src: LaukCriminalControlledRate) -> LaukcriminalcontrolledratebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukcriminalcontrolledratebaseOut(**src.model_dump())

def convert_laukcriminalcontrolledratebasein_to_sdk(src: LaukcriminalcontrolledrateBaseIn) -> LaukCriminalControlledRate:
    """Converts a clio_sdk model to clio_client model."""
    return LaukCriminalControlledRate(**src.model_dump())
