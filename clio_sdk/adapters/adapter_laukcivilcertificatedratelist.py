# Adapter for laukcivilcertificatedratelist
from clio_sdk.models.laukcivilcertificatedratelist import LaukcivilcertificatedratelistIn, LaukcivilcertificatedratelistOut, LaukcivilcertificatedratelistUpdate, LaukcivilcertificatedratelistDb
from clio_client.models.lauk_civil_certificated_rate_list import LaukCivilCertificatedRateList

def convert_sdk_to_laukcivilcertificatedratelistout(src: LaukCivilCertificatedRateList) -> LaukcivilcertificatedratelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukcivilcertificatedratelistOut(**src.model_dump())

def convert_laukcivilcertificatedratelistin_to_sdk(src: LaukcivilcertificatedratelistIn) -> LaukCivilCertificatedRateList:
    """Converts a clio_sdk model to clio_client model."""
    return LaukCivilCertificatedRateList(**src.model_dump())
