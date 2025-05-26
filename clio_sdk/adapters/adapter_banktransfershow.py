# Adapter for banktransfershow
from clio_sdk.models.banktransfershow import BanktransfershowIn, BanktransfershowOut, BanktransfershowUpdate, BanktransfershowDb
from clio_client.models import bank_transfer_show

def convert_sdk_to_banktransfershowout(src: bank_transfer_show) -> BanktransfershowOut:
    return BanktransfershowOut(**src.dict())

def convert_banktransfershowin_to_sdk(src: BanktransfershowIn) -> bank_transfer_show:
    return bank_transfer_show(**src.dict())
