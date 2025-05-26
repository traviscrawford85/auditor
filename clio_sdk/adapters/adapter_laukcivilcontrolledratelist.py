# Adapter for laukcivilcontrolledratelist
from clio_sdk.models.laukcivilcontrolledratelist import LaukcivilcontrolledratelistIn, LaukcivilcontrolledratelistOut, LaukcivilcontrolledratelistUpdate, LaukcivilcontrolledratelistDb
from clio_client.models import lauk_civil_controlled_rate_list

def convert_sdk_to_laukcivilcontrolledratelistout(src: lauk_civil_controlled_rate_list) -> LaukcivilcontrolledratelistOut:
    return LaukcivilcontrolledratelistOut(**src.dict())

def convert_laukcivilcontrolledratelistin_to_sdk(src: LaukcivilcontrolledratelistIn) -> lauk_civil_controlled_rate_list:
    return lauk_civil_controlled_rate_list(**src.dict())
