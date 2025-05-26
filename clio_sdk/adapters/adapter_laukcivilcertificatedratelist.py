# Adapter for laukcivilcertificatedratelist
from clio_sdk.models.laukcivilcertificatedratelist import LaukcivilcertificatedratelistIn, LaukcivilcertificatedratelistOut, LaukcivilcertificatedratelistUpdate, LaukcivilcertificatedratelistDb
from clio_client.models import lauk_civil_certificated_rate_list

def convert_sdk_to_laukcivilcertificatedratelistout(src: lauk_civil_certificated_rate_list) -> LaukcivilcertificatedratelistOut:
    return LaukcivilcertificatedratelistOut(**src.dict())

def convert_laukcivilcertificatedratelistin_to_sdk(src: LaukcivilcertificatedratelistIn) -> lauk_civil_certificated_rate_list:
    return lauk_civil_certificated_rate_list(**src.dict())
