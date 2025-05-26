# Adapter for laukcriminalcontrolledratelist
from clio_sdk.models.laukcriminalcontrolledratelist import LaukcriminalcontrolledratelistIn, LaukcriminalcontrolledratelistOut, LaukcriminalcontrolledratelistUpdate, LaukcriminalcontrolledratelistDb
from clio_client.models.lauk_criminal_controlled_rate_list import LaukCriminalControlledRateList

def convert_sdk_to_laukcriminalcontrolledratelistout(src: LaukCriminalControlledRateList) -> LaukcriminalcontrolledratelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukcriminalcontrolledratelistOut(**src.model_dump())

def convert_laukcriminalcontrolledratelistin_to_sdk(src: LaukcriminalcontrolledratelistIn) -> LaukCriminalControlledRateList:
    """Converts a clio_sdk model to clio_client model."""
    return LaukCriminalControlledRateList(**src.model_dump())
