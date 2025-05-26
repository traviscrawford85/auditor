# Adapter for billingsettingshow
from clio_sdk.models.billingsettingshow import BillingsettingshowIn, BillingsettingshowOut, BillingsettingshowUpdate, BillingsettingshowDb
from clio_client.models.billing_setting_show import BillingSettingShow

def convert_sdk_to_billingsettingshowout(src: BillingSettingShow) -> BillingsettingshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillingsettingshowOut(**src.model_dump())

def convert_billingsettingshowin_to_sdk(src: BillingsettingshowIn) -> BillingSettingShow:
    """Converts a clio_sdk model to clio_client model."""
    return BillingSettingShow(**src.model_dump())
