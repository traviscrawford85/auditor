# Adapter for laukcivilcontrolledratebase
from clio_sdk.models.laukcivilcontrolledratebase import LaukcivilcontrolledrateBaseIn, LaukcivilcontrolledratebaseOut, LaukcivilcontrolledratebaseUpdate, LaukcivilcontrolledratebaseDb
from clio_client.models.lauk_civil_controlled_rate import LaukCivilControlledRate

def convert_sdk_to_laukcivilcontrolledratebaseout(src: LaukCivilControlledRate) -> LaukcivilcontrolledratebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukcivilcontrolledratebaseOut(**src.model_dump())

def convert_laukcivilcontrolledratebasein_to_sdk(src: LaukcivilcontrolledrateBaseIn) -> LaukCivilControlledRate:
    """Converts a clio_sdk model to clio_client model."""
    return LaukCivilControlledRate(**src.model_dump())
