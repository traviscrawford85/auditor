# Adapter for laukcivilcertificatedratebase
from clio_sdk.models.laukcivilcertificatedratebase import LaukcivilcertificatedratebaseIn, LaukcivilcertificatedratebaseOut, LaukcivilcertificatedratebaseUpdate, LaukcivilcertificatedratebaseDb
from clio_client.models import lauk_civil_certificated_rate

def convert_sdk_to_laukcivilcertificatedratebaseout(src: lauk_civil_certificated_rate) -> LaukcivilcertificatedratebaseOut:
    return LaukcivilcertificatedratebaseOut(**src.dict())

def convert_laukcivilcertificatedratebasein_to_sdk(src: LaukcivilcertificatedratebaseIn) -> lauk_civil_certificated_rate:
    return lauk_civil_certificated_rate(**src.dict())
