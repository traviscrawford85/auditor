# Adapter for laukcivilcontrolledratelist
from clio_sdk.models.laukcivilcontrolledratelist import LaukcivilcontrolledratelistIn, LaukcivilcontrolledratelistOut, LaukcivilcontrolledratelistUpdate, LaukcivilcontrolledratelistDb
from clio_client.models.lauk_civil_controlled_rate_list import LaukCivilControlledRateList

def convert_sdk_to_laukcivilcontrolledratelistout(src: LaukCivilControlledRateList) -> LaukcivilcontrolledratelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukcivilcontrolledratelistOut(**src.model_dump())

def convert_laukcivilcontrolledratelistin_to_sdk(src: LaukcivilcontrolledratelistIn) -> LaukCivilControlledRateList:
    """Converts a clio_sdk model to clio_client model."""
    return LaukCivilControlledRateList(**src.model_dump())
