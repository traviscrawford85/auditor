# Adapter for banktransferbase
from clio_sdk.models.banktransferbase import BanktransferbaseIn, BanktransferbaseOut, BanktransferbaseUpdate, BanktransferbaseDb
from clio_client.models import bank_transfer

def convert_sdk_to_banktransferbaseout(src: bank_transfer) -> BanktransferbaseOut:
    return BanktransferbaseOut(**src.dict())

def convert_banktransferbasein_to_sdk(src: BanktransferbaseIn) -> bank_transfer:
    return bank_transfer(**src.dict())
