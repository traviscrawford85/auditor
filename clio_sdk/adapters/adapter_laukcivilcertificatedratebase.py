# Adapter for laukcivilcertificatedratebase
from clio_sdk.models.laukcivilcertificatedratebase import LaukcivilcertificatedrateBaseIn, LaukcivilcertificatedratebaseOut, LaukcivilcertificatedratebaseUpdate, LaukcivilcertificatedratebaseDb
from clio_client.models.lauk_civil_certificated_rate import LaukCivilCertificatedRate

def convert_sdk_to_laukcivilcertificatedratebaseout(src: LaukCivilCertificatedRate) -> LaukcivilcertificatedratebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukcivilcertificatedratebaseOut(**src.model_dump())

def convert_laukcivilcertificatedratebasein_to_sdk(src: LaukcivilcertificatedrateBaseIn) -> LaukCivilCertificatedRate:
    """Converts a clio_sdk model to clio_client model."""
    return LaukCivilCertificatedRate(**src.model_dump())
