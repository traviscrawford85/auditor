# Adapter for billingsettingbase
from clio_sdk.models.billingsettingbase import BillingsettingBaseIn, BillingsettingbaseOut, BillingsettingbaseUpdate, BillingsettingbaseDb
from clio_client.models.billing_setting import BillingSetting

def convert_sdk_to_billingsettingbaseout(src: BillingSetting) -> BillingsettingbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillingsettingbaseOut(**src.model_dump())

def convert_billingsettingbasein_to_sdk(src: BillingsettingBaseIn) -> BillingSetting:
    """Converts a clio_sdk model to clio_client model."""
    return BillingSetting(**src.model_dump())
