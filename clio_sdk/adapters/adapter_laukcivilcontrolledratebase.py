# Adapter for laukcivilcontrolledratebase
from clio_sdk.models.laukcivilcontrolledratebase import LaukcivilcontrolledratebaseIn, LaukcivilcontrolledratebaseOut, LaukcivilcontrolledratebaseUpdate, LaukcivilcontrolledratebaseDb
from clio_client.models import lauk_civil_controlled_rate

def convert_sdk_to_laukcivilcontrolledratebaseout(src: lauk_civil_controlled_rate) -> LaukcivilcontrolledratebaseOut:
    return LaukcivilcontrolledratebaseOut(**src.dict())

def convert_laukcivilcontrolledratebasein_to_sdk(src: LaukcivilcontrolledratebaseIn) -> lauk_civil_controlled_rate:
    return lauk_civil_controlled_rate(**src.dict())
