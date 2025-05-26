# Adapter for laukcriminalcontrolledratelist
from clio_sdk.models.laukcriminalcontrolledratelist import LaukcriminalcontrolledratelistIn, LaukcriminalcontrolledratelistOut, LaukcriminalcontrolledratelistUpdate, LaukcriminalcontrolledratelistDb
from clio_client.models import lauk_criminal_controlled_rate_list

def convert_sdk_to_laukcriminalcontrolledratelistout(src: lauk_criminal_controlled_rate_list) -> LaukcriminalcontrolledratelistOut:
    return LaukcriminalcontrolledratelistOut(**src.dict())

def convert_laukcriminalcontrolledratelistin_to_sdk(src: LaukcriminalcontrolledratelistIn) -> lauk_criminal_controlled_rate_list:
    return lauk_criminal_controlled_rate_list(**src.dict())
