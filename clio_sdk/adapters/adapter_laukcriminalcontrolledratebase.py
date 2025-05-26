# Adapter for laukcriminalcontrolledratebase
from clio_sdk.models.laukcriminalcontrolledratebase import LaukcriminalcontrolledratebaseIn, LaukcriminalcontrolledratebaseOut, LaukcriminalcontrolledratebaseUpdate, LaukcriminalcontrolledratebaseDb
from clio_client.models import lauk_criminal_controlled_rate

def convert_sdk_to_laukcriminalcontrolledratebaseout(src: lauk_criminal_controlled_rate) -> LaukcriminalcontrolledratebaseOut:
    return LaukcriminalcontrolledratebaseOut(**src.dict())

def convert_laukcriminalcontrolledratebasein_to_sdk(src: LaukcriminalcontrolledratebaseIn) -> lauk_criminal_controlled_rate:
    return lauk_criminal_controlled_rate(**src.dict())
